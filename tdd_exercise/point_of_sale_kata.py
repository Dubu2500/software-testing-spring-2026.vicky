# -*- coding: utf-8 -*-

"""
Modulo de una app que escanea codigos de barra para vender productos
"""

import json
import os


def read_from_json(key_and_file_name="products"):
    """Cargar data del json"""
    file_path = os.path.join(os.path.dirname(__file__), f"{key_and_file_name}.json")
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data[key_and_file_name]


def scan_barcode(barcode):
    """
    Metodo que escanea un codigo de barras y devuelve el precio o el error
    """

    products = read_from_json("products")

    # 1
    if barcode in products:
        return f"${products[barcode]:.2f}"