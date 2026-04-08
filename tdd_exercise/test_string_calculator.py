
"""
Este modulo contiene las pruebas del ejercicio de String Calculator
"""

import unittest
import string_calculator


class TestStringCalculator(unittest.TestCase):
    """
    Casos de prueba para la funcion add
    """

    def test_empty_string_returns_zero(self):
        """
        1. Metodo que recibe un string vacio y devuelve 0
        """
        self.assertEqual(string_calculator.add(""), 0)
