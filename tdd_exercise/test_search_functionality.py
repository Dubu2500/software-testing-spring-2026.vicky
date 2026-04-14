# -*- coding: utf-8 -*-

"""
Este modulo contiene las pruebas del ejercicio de search functionality para buscar ciudades
"""

import unittest

from search_functionality import read_from_json, search


class TestSearchFunctionality(unittest.TestCase):
    """
    Casos de prueba para ejercicio de Search Functionality
    """

    @classmethod
    def setUpClass(cls):
        # Cargar ciudades del archivo json, read_from_json
        cities = read_from_json("cities")

        cls.test_data = [
            # 1. < 2 caracteres deben regresar no result
            {"input": "", "output": []},
            {"input": "a", "output": []},
            # 2. >= 2 caracteres deberan regresar ciudades con busqueda de texto
            {"input": "Va", "output": ["Valencia", "Vancouver"]},
            {"input": "Pa", "output": ["Paris"]},
            # 3. Busqueda Case insensitive
            {"input": "va", "output": ["Valencia", "Vancouver"]},
            {"input": "PARIS", "output": ["Paris"]},
            {"input": "NeW", "output": ["New York City"]},
            # 4. Buscar texto como parte del nombre de la ciudad
            {"input": "ape", "output": ["Budapest"]},
            {"input": "ster", "output": ["Amsterdam"]},
            {"input": "kok", "output": ["Bangkok"]},
            {"input": "dam", "output": ["Rotterdam", "Amsterdam"]},
            # 5. Devuelve todos los paises
            {"input": "*", "output": cities},
            # Edge cases
            {"input": "xyz", "output": []},
        ]

    def test_search(self):
        """
        Funcion que realiza ciclo para hacer pruebas con variedad de inputs
        """
        for x in self.test_data:
            with self.subTest(input=x["input"], output=x["output"]):
                self.assertEqual(search(x["input"]), x["output"])
