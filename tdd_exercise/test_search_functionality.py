# -*- coding: utf-8 -*-

"""
Este modulo contiene las pruebas del ejercicio de search functionality para buscar ciudades
"""

import unittest

from search_functionality import search


class TestSearchFunctionality(unittest.TestCase):
    """
    Casos de prueba para ejercicio de Search Functionality
    """

    @classmethod
    def setUpClass(cls):
        cls.test_data = [
            # Requerimiento 1: < 2 caracteres deben regresar no result
            {"input": "", "output": []},
            {"input": "a", "output": []},
            # Requerimiento 2: >= 2 caracteres deberan regresar ciudades con busqueda de texto
            {"input": "Va", "output": ["Valencia", "Vancouver"]},
            {"input": "Pa", "output": ["Paris"]},
            # Requerimiento 3: busqueda Case insensitive
            {"input": "va", "output": ["Valencia", "Vancouver"]},
            {"input": "PARIS", "output": ["Paris"]},
            {"input": "NeW", "output": ["New York City"]},
            # Edge cases
            {"input": "xyz", "output": []},
        ]

    def test_search(self):
        """
        Tests the search_cities function with various inputs and expected outputs.
        """
        for x in self.test_data:
            with self.subTest(input=x["input"], output=x["output"]):
                self.assertEqual(search(x["input"]), x["output"])
