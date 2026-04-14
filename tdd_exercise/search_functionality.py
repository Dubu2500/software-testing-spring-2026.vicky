# -*- coding: utf-8 -*-

"""
Este modulo contiene la logica para las pruebas del ejercicio de FizzBuzz
"""

import json
import os


def read_from_json(key_and_file_name="cities"):
    """Leer ciudades del archivo json"""
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

    # Cargar ciudades del json
    cities_file_path = os.path.join(os.path.dirname(__file__), "cities.json")
    with open(cities_file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        cities = data["cities"]

    cities_found = []

    # 5. Si el input es "*", devolver todas las ciudades
    if str_to_search == "*":
        return cities

    # 1. Si el input es menor a 2 caracteres devolver vacio
    if len(str_to_search) < 2:
        return cities_found

    # 3. Convertir input a minusculas para busqueda case-insensitive
    search_lower = str_to_search.lower()

    for city in cities:
        city_lower = city.lower()
        # 2. Ciudades que empiezan con el input
        # 4. Ciudades que contienen el input
        if city_lower.startswith(search_lower) or search_lower in city_lower:
            cities_found.append(city)

    return cities_found
