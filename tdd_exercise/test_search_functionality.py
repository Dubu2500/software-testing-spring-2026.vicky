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
            # Requirement 2: >= 2 characters should return cities starting with search text
            {"input": "Va", "output": ["Valencia", "Vancouver"]},
            {"input": "Pa", "output": ["Paris"]},
            # Requirement 3: Case insensitive search
            {"input": "va", "output": ["Valencia", "Vancouver"]},
            {"input": "PARIS", "output": ["Paris"]},
            {"input": "NeW", "output": ["New York City"]},
            # Requirement 4: Search text as part of city name (substring search)
            {"input": "ape", "output": ["Budapest"]},
            {"input": "ster", "output": ["Amsterdam"]},
            {"input": "kok", "output": ["Bangkok"]},
            {"input": "dam", "output": ["Rotterdam", "Amsterdam"]},
            # Requirement 5: Asterisk should return all cities
            {"input": "*", "output": cities},
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
