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

    def test_numbers_comma_separated_returns_sum(self):
        """
        2. Metodo que recibe uno o dos numeros separados por coma y devuelve su suma
        """
        self.assertEqual(string_calculator.add("1"), 1)
        self.assertEqual(string_calculator.add("1,2"), 3)

    def test_unknown_number_of_arguments_returns_sum(self):
        """
        3. Metodo que recibe cantidad indefinida de numeros separados por comas
        """
        self.assertEqual(string_calculator.add("1,2,3,4"), 10)

    def test_newline_as_separator_returns_sum(self):
        """
        4. Metodo que acepta saltos de linea como separadores ademas de comas
        """
        self.assertEqual(string_calculator.add("1\n2,3"), 6)

    def test_no_trailing_separator_returns_exception(self):
        """
        5. Metodo que valida que no haya separador al final y lanza excepcion
        """
        with self.assertRaises(ValueError) as ctx:
            string_calculator.add("1,2,")
        self.assertEqual(str(ctx.exception), "Separator at end not allowed")

    def test_custom_delimiter_returns_sum(self):
        """
        6. Metodo que permite cambiar el delimitador con formato "//X\\n"
        """
        self.assertEqual(string_calculator.add("//;\n1;3"), 4)
        self.assertEqual(string_calculator.add("//|\n1|2|3"), 6)
        self.assertEqual(string_calculator.add("//sep\n2sep5"), 7)
