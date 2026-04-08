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

    def test_custom_delimiter_invalid_character_returns_exception(self):
        """
        7. Metodo que valida caracteres no esperados en el delimitador personalizado
        """
        with self.assertRaises(ValueError) as ctx:
            string_calculator.add("//|\n1|2,3")
        self.assertEqual(str(ctx.exception), "expected '|' but found ',' at position 3")

    def test_negative_numbers_not_allowed_returns_exception(self):
        """
        8. Metodo que no permite numeros negativos y muestra los negativos encontrados
        """
        with self.assertRaises(ValueError) as ctx:
            string_calculator.add("1,-2")
        self.assertEqual(str(ctx.exception), "Negative number(s) not allowed: -2")

        with self.assertRaises(ValueError) as ctx:
            string_calculator.add("2,-4,-9")
        self.assertEqual(str(ctx.exception), "Negative number(s) not allowed: -4,-9")

    def test_multiple_errors_newline_separated_returns_errors(self):
        """
        9. Metodo que retorna multiples errores separados por saltos de linea
        """
        with self.assertRaises(ValueError) as ctx:
            string_calculator.add("//|\n1|2,-3")
        error_msg = str(ctx.exception)
        self.assertIn("Negative number(s) not allowed: -3", error_msg)
        self.assertIn("expected '|' but found ',' at position 3", error_msg)
        self.assertIn("\n", error_msg)

    def test_ignore_numbers_greater_than_1000_returns_sum(self):
        """
        10. Metodo que ignora numeros mayores a 1000 en la suma
        """
        self.assertEqual(string_calculator.add("2,1001"), 2)
        self.assertEqual(string_calculator.add("1000,1001,2"), 1002)
