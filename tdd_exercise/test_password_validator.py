"""
Este modulo contiene las pruebas del ejercicio de validacion de contraseñas
"""

import unittest

import password_validator as pv


class TestPasswordValidator(unittest.TestCase):
    """
    Casos de prueba para la funcion validate_password
    """

    def test_valid_password(self):
        """
        1. Metodo que recibe una contraseña valida y devuelve valid=True, errors vacio
        """
        result = pv.validate_password("Abc123!@")
        self.assertTrue(result["valid"])
        self.assertEqual(result["errors"], "")

    def test_at_least_8_characters(self):
        """
        2. Metodo que detecta contraseña con menos de 8 caracteres
        """
        result = pv.validate_password("Ab1!@")
        self.assertFalse(result["valid"])
        self.assertIn("Password must be at least 8 characters", result["errors"])

    def test_at_least_two_numbers(self):
        """
        3. Metodo que detecta contraseña con menos de 2 numeros
        """
        result = pv.validate_password("Abcdefgh1")
        self.assertFalse(result["valid"])
        self.assertIn("The password must contain at least 2 numbers", result["errors"])

    def test_at_least_one_capital_letter(self):
        """
        4. Metodo que detecta ausencia de mayuscula
        """
        result = pv.validate_password("abcdefgh12!")
        self.assertFalse(result["valid"])
        self.assertIn(
            "password must contain at least one capital letter", result["errors"]
        )

    def test_at_least_one_special_character(self):
        """
        5. Metodo que detecta ausencia de caracter especial
        """
        result = pv.validate_password("Abcdefgh12")
        self.assertFalse(result["valid"])
        self.assertIn(
            "password must contain at least one special character", result["errors"]
        )
