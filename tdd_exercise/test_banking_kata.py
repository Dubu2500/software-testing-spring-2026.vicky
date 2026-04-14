# -*- coding: utf-8 -*-

"""
Pruebas Test Driven Development para el ejercicio Banking Kata
"""

import sys
import unittest
from io import StringIO
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

    @patch("banking_kata.datetime")
    def test_print_statement_output_format(self, mock_datetime):
        """
        3. Impresion del estado de cuenta: formato y orden
        """
        # Simular fechas fijas para las transacciones
        mock_datetime.now.return_value.strftime.side_effect = [
            "01/04/2014",
            "02/04/2014",
            "10/04/2014",
        ]
        self.account.deposit(1000)
        self.account.withdraw(100)
        self.account.deposit(500)

        # Capturar stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        self.account.print_statement()
        sys.stdout = sys.__stdout__

        expected_output = (
            "DATE | AMOUNT | BALANCE\n"
            "10/04/2014 | 500.00 | 1400.00\n"
            "02/04/2014 | -100.00 | 900.00\n"
            "01/04/2014 | 1000.00 | 1000.00\n"
        )
        self.assertEqual(captured_output.getvalue(), expected_output)

    @patch("banking_kata.datetime")
    def test_multiple_transactions_balance_correct(self, mock_datetime):
        """
        Prueba combinada: depositos y retiros en secuencia
        """
        mock_datetime.now.return_value.strftime.return_value = "01/01/2020"
        self.account.deposit(500)
        self.account.withdraw(200)
        self.account.deposit(100)
        self.account.withdraw(50)
        self.assertEqual(self.account._balance, 350)
        self.assertEqual(len(self.account._transactions), 4)

    def test_print_statement_empty_account(self):
        """
        Impresion de estado de cuenta cuando no hay transacciones
        """
        captured_output = StringIO()
        sys.stdout = captured_output
        self.account.print_statement()
        sys.stdout = sys.__stdout__
        expected_output = "DATE | AMOUNT | BALANCE\n"
        self.assertEqual(captured_output.getvalue(), expected_output)
