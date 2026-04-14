# -*- coding: utf-8 -*-

"""
Este modulo contiene la logica para las pruebas del ejercicio de FizzBuzz
"""

import json
import os


def read_from_json(key_and_file_name="cities"):
    """Read city names from a JSON file."""
    cities_file_path = os.path.join(
        os.path.dirname(__file__), f"{key_and_file_name}.json"
    )
    with open(cities_file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data[key_and_file_name]


def search(str_to_search):
    """
    Metodo que recibe un string y devuelve el numero de ciudades encontradas
    """

    # Load cities from JSON file
    cities_file_path = os.path.join(os.path.dirname(__file__), "cities.json")
    with open(cities_file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        cities = data["cities"]

    cities_found = []

    # Requirement 1: If search text is fewer than 2 characters, return no results
    if len(str_to_search) < 2:
        return cities_found

    # Convert search text to lowercase for case-insensitive search (Requirement 3)
    search_lower = str_to_search.lower()

    for city in cities:
        city_lower = city.lower()
        # Requeriment 2
        if city_lower.startswith(search_lower):
            # Requeriment 4
            cities_found.append(city)

    return cities_found
