"""
Este modulo contiene las pruebas del ejercicio de FizzBuzz
"""

import unittest

from fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    """
    Casos de prueba para ejercicio de FizzBuzz
    """

    def test_from_number_return_string(self):
        """
        1. Metodo que recibe un numero de input y lo devuelve en string
        """
        self.assertEqual(fizz_buzz(1), "1")
        self.assertEqual(fizz_buzz(-1), "-1")

    def test_from_number_multiple_three_return_fizz(
        self,
    ):
        """
        2. Metodo que recibe un numero multiplo de 3 de input y devuelve "Fizz"
        """
        self.assertEqual(fizz_buzz(-3), "Fizz")
        self.assertEqual(fizz_buzz(0), "Fizz")
        self.assertEqual(fizz_buzz(3), "Fizz")

    def test_from_number_multiple_three_return_buzz(
        self,
    ):
        """
        3. Metodo que recibe un numero multiplo de 5 de input y devuelve "Buzz"
        """
        self.assertEqual(fizz_buzz(-5), "Buzz")
        self.assertEqual(fizz_buzz(0), "Buzz")
        self.assertEqual(fizz_buzz(5), "Buzz")

    def test_from_number_multiple_three_five_return_fizz_buzz(
        self,
    ):
        """
        4. Metodo que recibe un numero multiplo de 3 o de 5 de input y devuelve "FizzBuzz"
        """
        self.assertEqual(fizz_buzz(-15), "FizzBuzz")
        self.assertEqual(fizz_buzz(0), "FizzBuzz")
        self.assertEqual(fizz_buzz(15), "FizzBuzz")
