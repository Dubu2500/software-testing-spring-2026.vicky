# -*- coding: utf-8 -*-

"""
Pruebas Test Driven Development para el ejercicio Point of Sale Kata
"""

import unittest

import point_of_sale_kata
from point_of_sale_kata import scan_barcode

# pylint: disable=protected-access


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
            # 2. Codigo de barra '23456' -> $12.50
            {"input": "23456", "output": "$12.50"},
            # 3. Codigo de barra desconocido -> error
            {"input": "99999", "output": "Error: barcode not found"},
            # 4. Codigo de barra vacio -> error
            {"input": "", "output": "Error: empty barcode"},
            {"input": "   ", "output": "Error: empty barcode"},
            # 5. Codigos de barra desconocido
            {"input": "54321", "output": "Error: barcode not found"},
            {"input": "ABCDE", "output": "Error: barcode not found"},
        ]

        # Datos de prueba para el comando TOTAL (requisito 5)
        cls.total_test_sequences = [
            {
                "name": "Dos productos válidos",
                "calls": [("12345", "$7.25"), ("23456", "$12.50"), ("TOTAL", "$19.75")],
            },
            {
                "name": "Un solo producto",
                "calls": [("12345", "$7.25"), ("TOTAL", "$7.25")],
            },
            {"name": "Sin productos escaneados", "calls": [("TOTAL", "$0.00")]},
            {
                "name": "Producto inválido no se agrega al total",
                "calls": [
                    ("12345", "$7.25"),
                    ("99999", "Error: barcode not found"),
                    ("TOTAL", "$7.25"),
                ],
            },
            {
                "name": "Múltiples productos repetidos",
                "calls": [("12345", "$7.25"), ("12345", "$7.25"), ("TOTAL", "$14.50")],
            },
        ]

    def test_scan_barcode(self):
        """Pruebas Data-driven para la funcion scan_barcode (requisitos 1-4)"""
        for test in self.test_data:
            with self.subTest(barcode=test["input"]):
                self.assertEqual(scan_barcode(test["input"]), test["output"])

    def test_total_command(self):
        """Pruebas del comando TOTAL (requisito 5) con secuencias de llamadas"""
        for seq in self.total_test_sequences:
            with self.subTest(name=seq["name"]):
                # Reiniciar el estado global antes de cada secuencia
                point_of_sale_kata._scanned_barcodes = []
                for barcode, expected in seq["calls"]:
                    self.assertEqual(scan_barcode(barcode), expected)
