# -*- coding: utf-8 -*-

"""
Este modulo contiene la logica para las pruebas del ejercicio de FizzBuzz
"""

import json
import os


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

    city_search = str_to_search

    for city in cities:
        if city_search in city:
            cities_found.append(city)

    return cities_found
