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

    return {"valid": valid, "errors": error_msg}
