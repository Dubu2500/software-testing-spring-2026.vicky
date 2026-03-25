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
