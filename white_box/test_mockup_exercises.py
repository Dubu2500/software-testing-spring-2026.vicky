# -*- coding: utf-8 -*-

"""
Mock up testing examples.
"""
import subprocess
import unittest
from unittest.mock import Mock, mock_open, patch

from white_box.mockup_exercises import (
    execute_command,
    fetch_data_from_api,
    perform_action_based_on_time,
    read_data_from_file,
)


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


class TestFetchDataFromAPI(unittest.TestCase):
    """
    Fetch Data From API unittest class.
    """

    @patch("white_box.mockup_exercises.requests.get")
    def test_fetch_data_from_api_success(self, mock_get):
        """
        Check data fetching from API.
        """
        mock_response = Mock()
        mock_response.json.return_value = {"key": "value"}
        mock_get.return_value = mock_response

        result = fetch_data_from_api("http://test.com")
        self.assertEqual(result, {"key": "value"})
        mock_get.assert_called_once_with("http://test.com", timeout=10)


class TestReadDataFromFile(unittest.TestCase):
    """
    Read Data From File unittest class.
    """

    @patch("builtins.open", new_callable=mock_open, read_data="test data")
    def test_read_data_from_file_success(self, mock_file):
        """
        Check file reading success.
        """
        result = read_data_from_file("test.txt")
        self.assertEqual(result, "test data")
        mock_file.assert_called_once_with("test.txt", encoding="utf-8")

    @patch("builtins.open")
    def test_read_data_from_file_not_found(self, mock_file):
        """
        Check file reading when file is not found.
        """
        mock_file.side_effect = FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            read_data_from_file("missing.txt")


class TestExecuteCommand(unittest.TestCase):
    """
    Execute Command unittest class.
    """

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_success(self, mock_run):
        """
        Check command execution success.
        """
        mock_result = Mock()
        mock_result.stdout = "output"
        mock_run.return_value = mock_result

        result = execute_command(["echo", "hello"])
        self.assertEqual(result, "output")
        mock_run.assert_called_once_with(
            ["echo", "hello"], capture_output=True, check=False, text=True
        )

    @patch("white_box.mockup_exercises.subprocess.run")
    def test_execute_command_error(self, mock_run):
        """
        Check command execution when it fails.
        """
        mock_run.side_effect = subprocess.CalledProcessError(1, "cmd")
        with self.assertRaises(subprocess.CalledProcessError):
            execute_command(["fail_cmd"])
