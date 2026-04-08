# -*- coding: utf-8 -*-

"""
Este modulo contiene la logica para las pruebas del ejercicio de String Calculator
"""

import re


def _parse_custom_delimiter(message):
    """Extrae el delimitador personalizado y la parte numerica del mensaje."""
    parts = message.split("\n", 1)
    delimiter_part = parts[0][2:]
    numbers_part = parts[1]
    errors = []

    i = 0
    while i < len(numbers_part):
        character = numbers_part[i]
        if character.isdigit() or character == delimiter_part:
            i += 1
        else:
            errors.append(
                f"expected '{delimiter_part}' but found '{character}' at position {i}"
            )
            break

    return re.escape(delimiter_part), numbers_part, errors


def add(message):
    """
    Metodo que recibe un string con numeros,
    procesa segun los requerimientos de String Calculator y devuelve su suma
    """

    # 1. String vacio a 0
    if message == "":
        return 0

    errors = []
    delimiter = ",|\n"
    numbers_part = message

    # 5. Delimitador personalizado
    if message.startswith("//"):
        delimiter, numbers_part, errors = _parse_custom_delimiter(message)

    # 4. Validar separador al final
    if re.search(rf"{delimiter}$", numbers_part):
        errors.append("Separator at end not allowed")

    # 2 y 3. Dividir usando el delimitador
    raw_numbers = re.split(delimiter, numbers_part)

    integers = []
    negatives = []

    for item in raw_numbers:
        if item == "":
            continue
        if not item.lstrip("-").isdigit():
            errors.append(f"Invalid number: '{item}'")
            continue
        num = int(item)
        if num < 0:
            negatives.append(num)
        elif num <= 1000:
            integers.append(num)

    # 6. Numeros negativos no permitidos
    if negatives:
        errors.append(
            f"Negative number(s) not allowed: {','.join(map(str, negatives))}"
        )

    # 7. Multiples errores separados por newline
    if errors:
        raise ValueError("\n".join(errors))

    # 8. Numeros mayores a 1000 ignorados
    return sum(integers)
