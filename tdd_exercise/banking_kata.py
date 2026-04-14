# -*- coding: utf-8 -*-

"""
Modulo que implementa una cuenta bancaria simple con operaciones para el ejercicio Banking Kata
"""

from datetime import datetime


class Account:
    """
    Clase que representa una cuenta bancaria
    """

    def __init__(self):
        """Inicializa la cuenta con saldo cero y lista de transacciones vacia"""
        self._balance = 0
        self._transactions = []

    # 1. Deposito en la cuenta
    def deposit(self, amount: int):
        """
        Realiza un deposito
        """
        self._balance += amount
        self._transactions.append(
            (datetime.now().strftime("%d/%m/%Y"), amount, self._balance)
        )

    # 2. Retiro de la cuenta
    def withdraw(self, amount: int):
        """
        Realiza un retiro
        """
        self._balance -= amount
        self._transactions.append(
            (datetime.now().strftime("%d/%m/%Y"), -amount, self._balance)
        )

    # 3. Imprimir estado de cuenta en consola
    def print_statement(self):
        """
        Imprime el estado de cuenta con formato
        """
        print("DATE | AMOUNT | BALANCE")
        for date, amount, balance in reversed(self._transactions):
            print(f"{date} | {amount:.2f} | {balance:.2f}")