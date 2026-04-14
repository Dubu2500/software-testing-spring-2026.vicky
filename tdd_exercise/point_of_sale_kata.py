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
    # 4. Codigo de barra vacio
    if not barcode or barcode.strip() == "":
        return "Error: empty barcode"

    # Requisito 5: comando TOTAL
    if barcode.strip().upper() == "TOTAL":
        if not _scanned_barcodes:
            return "$0.00"
        products = read_from_json("products")
        total = sum(products[bc] for bc in _scanned_barcodes)
        _scanned_barcodes = []  # reiniciar después del total
        return f"${total:.2f}"
    
    products = read_from_json("products")

    # 1 & 2. Codigo de barras
    if barcode in products:
        return f"${products[barcode]:.2f}"

    # 3. Codigo de barra desconocido
    return "Error: barcode not found"
