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
