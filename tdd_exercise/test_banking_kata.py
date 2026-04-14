# -*- coding: utf-8 -*-

"""
Pruebas Test Driven Development para el ejercicio Banking Kata
"""

import unittest
from unittest.mock import patch

from banking_kata import Account

# pylint: disable=protected-access


class TestBankingKata(unittest.TestCase):
    """
    Casos de prueba para la clase Account.
    """

    def setUp(self):
        """Crea una cuenta nueva antes de cada prueba."""
        self.account = Account()

    @patch("banking_kata.datetime")
    def test_deposit_increases_balance(self, mock_datetime):
        """
        1. Deposito en cuenta: el saldo debe aumentar
        """
        # Fijar fecha para evitar dependencia del dia actual
        mock_datetime.now.return_value.strftime.return_value = "01/04/2014"
        self.account.deposit(1000)
        # Verificar saldo
        self.assertEqual(self.account._balance, 1000)
        self.assertEqual(len(self.account._transactions), 1)
        self.assertEqual(self.account._transactions[0]["amount"], 1000)
        self.assertEqual(self.account._transactions[0]["balance"], 1000)

    @patch("banking_kata.datetime")
    def test_withdraw_decreases_balance(self, mock_datetime):
        """
        2. Retiro de la cuenta: el saldo debe disminuir
        """
        mock_datetime.now.return_value.strftime.return_value = "02/04/2014"
        self.account.deposit(1000)
        self.account.withdraw(100)
        self.assertEqual(self.account._balance, 900)
        self.assertEqual(len(self.account._transactions), 2)
        self.assertEqual(self.account._transactions[1]["amount"], -100)
        self.assertEqual(self.account._transactions[1]["balance"], 900)
