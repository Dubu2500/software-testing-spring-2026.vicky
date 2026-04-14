# -*- coding: utf-8 -*-

"""
Pruebas Test Driven Development para el ejercicio Banking Kata
"""

import unittest
from unittest.mock import patch
from banking_kata import Account


class TestBankingKata(unittest.TestCase):
    """
    Casos de prueba para la clase Account.
    """

    def setUp(self):
        """Crea una cuenta nueva antes de cada prueba."""
        self.account = Account()

    @patch('banking_kata.datetime')
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
