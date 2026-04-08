# -*- coding: utf-8 -*-

"""
Test Driven Development (TDD) tests.
"""
import unittest

from tdd.exercises import add, cities, fizzbuzz, search_cities


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

    4. Add validation to not to allow a separator at the end.
    For example "1,2," should return an error (or throw an exception).

    5. Allow the add method to handle different delimiters. To change the delimiter,
    the beginning of the input will contain a separate line that looks like this:
    //[delimiter]\n[numbers]

    Examples:
    - "//;\n1;3" should return "4"
    - "//|\n1|2|3" should return "6"
    - "//sep\n2sep5" should return "7"
    - "//|\n1|2,3" is invalid and should return an error (or throw an exception) with the message
      "'|' expected but ',' found at position 3".
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

    def test_add_should_return_sum_when_numbers_contains_unknown_number_of_arguments(
        self,
    ):
        """
        Tests that add returns the sum for an unknown number of arguments.
        """
        self.assertEqual(add("1,2,3"), 6)

    def test_add_should_return_sum_when_numbers_contains_newlines_as_separators(self):
        """
        Tests that add returns the sum when numbers contains newlines as separators.
        """
        self.assertEqual(add("1,2\n3"), 6)
        self.assertEqual(add("2,\n3"), 5)

    def test_add_should_raise_exception_when_numbers_ends_with_a_separator(self):
        """
        Tests that add raises an exception when numbers ends with a separator.
        """
        with self.assertRaises(
            ValueError, msg="Input string cannot end with a separator."
        ):
            add("1,2,")

    # def test_add_should_return_sum_when_numbers_contains_different_delimiters(self):
    #    """
    #    Tests that add returns the sum when numbers contains different delimiters.
    #    """
    #    self.assertEqual(add("//;\n1;3"), 4)
    #    self.assertEqual(add("//|\n1|2|3"), 6)
    #    self.assertEqual(add("//sep\n2sep5"), 7)

    # def test_add_should_raise_exception_when_numbers_contains_invalid_delimiters(self):
    #    """
    #    Tests that add raises an exception when numbers contains invalid delimiters.
    #    """
    #    with self.assertRaisesRegex(ValueError, r"'|' expected but ',' found at position 3"):
    #        add("//|\n1|2,3")


class TestSearchCities(unittest.TestCase):
    """
    Kata 4 - Search functionality
    Implement a city search functionality. The function takes a string (search text) as input
    and returns the found cities which corresponds to the search text.

    Prerequisites:

    Create a collection of strings that will act as a database for the city names.
    City names: Paris, Budapest, Skopje, Rotterdam, Valencia, Vancouver, Amsterdam, Vienna, Sydney,
    New York City, London, Bangkok, Hong Kong, Dubai, Rome, Istanbul.

    Requirements:

    1. If the search text is fewer than 2 characters, then should return no results.
    (It is an optimization feature of the search functionality.)

    2. If the search text is equal to or more than 2 characters, then it should return all the city
    names starting with the exact search text.
    For example for search text "Va", the function should return Valencia and Vancouver.

    3. The search functionality should be case insensitive.

    4. The search functionality should work also when the search text is just a part of a city name
    For example "ape" should return "Budapest" city.

    5. If the search text is a "*" (asterisk), then it should return all the city names.
    """

    def setUp(self):
        self.test_data = [
            # Requirement 1: < 2 characters should return no results
            {"input": "", "output": []},
            {"input": "a", "output": []},
            # Requirement 2: >= 2 characters should return cities starting with search text
            {"input": "Va", "output": ["Valencia", "Vancouver"]},
            {"input": "Pa", "output": ["Paris"]},
            # Requirement 3: Case insensitive search
            {"input": "va", "output": ["Valencia", "Vancouver"]},
            {"input": "PARIS", "output": ["Paris"]},
            {"input": "NeW", "output": ["New York City"]},
            # Requirement 4: Search text as part of city name (substring search)
            {"input": "ape", "output": ["Budapest"]},
            {"input": "ster", "output": ["Amsterdam"]},
            {"input": "kok", "output": ["Bangkok"]},
            {"input": "dam", "output": ["Rotterdam", "Amsterdam"]},
            # Requirement 5: Asterisk should return all cities
            {"input": "*", "output": cities},
            # Edge cases
            {"input": "xyz", "output": []},
        ]

    def test_search_cities(self):
        """
        Tests the search_cities function with various inputs and expected outputs.
        """
        for x in self.test_data:
            with self.subTest(input=x["input"], output=x["output"]):
                self.assertEqual(search_cities(x["input"]), x["output"])
