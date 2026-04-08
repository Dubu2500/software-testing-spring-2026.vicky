"""
Este modulo contiene la logica para las pruebas del ejercicio de validacion de contraseñas
"""


def validate_password(password):
    """
    Metodo que recibe una contraseña y devuelve un diccionario con:
    - valid: bool indicando si es valida
    - errors: string con los mensajes de error (separados por newline)
    """

    errors = []

    # 1. Longitud minima 8 caracteres
    if len(password) < 8:
        errors.append("Password must be at least 8 characters")

    valid = len(errors) == 0
    error_msg = "\n".join(errors)

    # 2. Al menos 2 numeros
    digit_count = sum(1 for character in password if character.isdigit())
    if digit_count < 2:
        errors.append("The password must contain at least 2 numbers")

    # 3. Al menos una mayuscula
    if not any(character.isupper() for character in password):
        errors.append("password must contain at least one capital letter")

    return {"valid": valid, "errors": error_msg}
