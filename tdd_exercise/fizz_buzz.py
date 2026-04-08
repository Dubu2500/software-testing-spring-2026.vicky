"""
Este modulo contiene la logica para las pruebas del ejercicio de FizzBuzz
"""


def fizz_buzz(number):
    """
    Metodo que recibe numeros y devuelve un string segun los requerimientos de FizzBuzz
    """
    # 1. Numero a string
    output = str(number)

    # 2. Multiplos de 3
    if number % 3 == 0:
        output = "Fizz"

    return output
