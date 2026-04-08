"""
Este modulo contiene la logica para las pruebas del ejercicio de String Calculator
"""

import re


def add(message):
    """
    Recibe un string con numeros y devuelve su suma.
    """

    # 1. String vacio a 0
    if message == "":
        return 0

    errors = []
    delimiter = ","
    numbers_part = message

    # 2 y 3. Dividir usando el delimitador
    raw_numbers = re.split(delimiter, numbers_part)

    integers = []

    for item in raw_numbers:
        if item == "":
            continue
        if not item.lstrip("-").isdigit():
            errors.append(f"Invalid number: '{item}'")

    return sum(integers)