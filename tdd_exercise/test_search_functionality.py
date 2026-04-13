# -*- coding: utf-8 -*-

"""
Este modulo contiene las pruebas del ejercicio de search functionality para buscar ciudades
"""

import json
import os
import unittest

from search_functionality import search


class TestSearchFunctionality(unittest.TestCase):
    """
    Casos de prueba para ejercicio de Search Functionality
    """

    @classmethod
    def setUpClass(cls):
        # Load cities from JSON file
        cities_file_path = os.path.join(os.path.dirname(__file__), "cities.json")
        with open(cities_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            cities = data["cities"]

        cls.test_data = [
            # Requirement 1: < 2 characters should return no results
            {"input": "", "output": []},
            {"input": "a", "output": []},
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
