# -*- coding: utf-8 -*-

"""
Mock up testing examples.
"""
import unittest
from unittest.mock import patch

from white_box.mockup_exercises import perform_action_based_on_time


class TestPerformActionBasedOnTime(unittest.TestCase):
    """
    Perform Action Based On Time unittest class.
    """

    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_based_on_time_action_a(self, mock_time):
        """
        Action A.
        """
        # Set up the mock response
        mock_time.return_value = 5

        # Call the function under test
        result = perform_action_based_on_time()

        # Assert that the function returns the expected result
        self.assertEqual(result, "Action A")

    @patch("white_box.mockup_exercises.time.time")
    def test_perform_action_based_on_time_action_b(self, mock_time):
        """
        Action B.
        """
        # Set up the mock response
        mock_time.return_value = 15

        # Call the function under test
        result = perform_action_based_on_time()

        # Assert that the function returns the expected result
        self.assertEqual(result, "Action B")
