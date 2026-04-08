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

    """3. Multiplos de 5"""
    if input % 5:
        output = "Buzz"

    return output
