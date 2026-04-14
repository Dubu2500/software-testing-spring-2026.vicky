# -*- coding: utf-8 -*-

"""
Pruebas Test Driven Development para el ejercicio Point of Sale Kata
"""

import unittest

from point_of_sale_kata import scan_barcode


class TestPointOfSaleKata(unittest.TestCase):
    """
    Casos de prueba para la funcion Test Point of Sale Kata
    """

    @classmethod
    def setUpClass(cls):
        # Data de prueba en una sola variable
        cls.test_data = [
            # 1. Codigo de barra '12345' -> $7.25
            {"input": "12345", "output": "$7.25"},
        ]

    def test_scan_barcode(self):
        """Pruebas Data-driven para la funcion"""
        for test in self.test_data:
            with self.subTest(barcode=test["input"]):
                self.assertEqual(scan_barcode(test["input"]), test["output"])