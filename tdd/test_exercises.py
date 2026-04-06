# -*- coding: utf-8 -*-

"""
Test Driven Development (TDD) tests.
"""
import unittest

from tdd.exercises import add, fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    """
    Kata 1 - FizzBuzz
    FizzBuzz is one of the most famous coding exercises for beginners.
    It is a simple exercise but an excellent one to start learning the TDD flow with.

    Requirements
    1. Write a “fizzBuzz” method that accepts a number as input and returns it as a String.

    Notes:

    start with the minimal failing solution
    keep the three rules in mind and always write just sufficient enough code
    do not forget to refactor your code after each passing test
    write your assertions relating to the exact requirements
    2. For multiples of three return “Fizz” instead of the number

    3. For the multiples of five return “Buzz”

    4. For numbers that are multiples of both three and five return “FizzBuzz”.
    """

    def test_fizzbuzz_should_return_number_as_string_when_number_is_not_multiple_of_3_or_5(
        self,
    ):
        """
        Tests that fizzbuzz returns the number as a string for non-multiples of 3 or 5.
        """
        self.assertEqual(fizzbuzz(1), "1")
        self.assertEqual(fizzbuzz(2), "2")
        self.assertEqual(fizzbuzz(-2), "-2")

    def test_fizzbuzz_should_return_fizz_when_number_is_multiple_of_three(self):
        """
        Tests that fizzbuzz returns "Fizz" for multiples of three.
        """
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(6), "Fizz")
        self.assertEqual(fizzbuzz(9), "Fizz")
        self.assertEqual(fizzbuzz(-9), "Fizz")

    def test_fizzbuzz_should_return_buzz_when_number_is_multiple_of_five(self):
        """
        Tests that fizzbuzz returns "Buzz" for multiples of five.
        """
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(10), "Buzz")
        self.assertEqual(fizzbuzz(20), "Buzz")
        self.assertEqual(fizzbuzz(-20), "Buzz")

    def test_fizzbuzz_should_return_fizzbuzz_when_number_is_multiple_of_three_and_five(
        self,
    ):
        """
        Tests that fizzbuzz returns "FizzBuzz" for multiples of both three and five.
        """
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(30), "FizzBuzz")
        self.assertEqual(fizzbuzz(45), "FizzBuzz")
        self.assertEqual(fizzbuzz(-45), "FizzBuzz")


class TestAdd(unittest.TestCase):
    """
    Kata 2 - String calculator
    Create a simple calculator that takes a String and returns a integer.

    Requirements
    1. The method can take up to two numbers, separated by commas, and will return their sum as a
    result. So the inputs can be: “”, “1”, “1,2”. For an empty string, it will return 0.

    Notes:
    Start with the simplest case (empty string) and extend it with the more advanced cases
    (“1” and “1,2”) step by step keep the three rules in mind and always write just
    sufficient enough code do not forget to refactor your code after each passing test.

    2. Allow the add method to handle an unknown number of arguments.

    3. Allow the add method to handle newlines as separators, instead of comas.
    "1,2\n3" should return "6". "2,\n3" is invalid, but no need to clarify it with the program.
    """

    def test_add_should_return_0_when_numbers_is_an_empty_string(self):
        """
        Tests that add returns 0 for an empty string.
        """
        self.assertEqual(add(""), 0)

    def test_add_should_return_number_when_numbers_contains_a_single_number(self):
        """
        Tests that add returns the number for a single number.
        """
        self.assertEqual(add("1"), 1)

    def test_add_should_return_sum_when_numbers_contains_two_numbers(self):
        """
        Tests that add returns the sum for two numbers.
        """
        self.assertEqual(add("1,2"), 3)

    def test_add_should_return_sum_when_numbers_contains_unknown_number_of_arguments(self):
        """
        Tests that add returns the sum for an unknown number of arguments.
        """
        self.assertEqual(add("1,2,3"), 6)

    def test_add_should_return_sum_when_numbers_contains_newlines_as_separators(self):
        """
        Tests that add returns the sum when numbers contains newlines as separators.
        """
        self.assertEqual(add("1,2\n3"), 6)