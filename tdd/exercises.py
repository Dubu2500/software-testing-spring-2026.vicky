# -*- coding: utf-8 -*-

"""
Test Driven Development (TDD) exercises.
"""


def fizzbuzz(num):
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
    output = ""

    if num % 3 == 0:
        output += "Fizz"

    if num % 5 == 0:
        output += "Buzz"

    if output == "":
        output = str(num)

    return output


def add(numbers):
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
    if numbers == "":
        return 0

    numbers = numbers.replace("\n", ",")

    if numbers.endswith(","):
        raise ValueError("Input string cannot end with a separator.")

    num_list = numbers.split(",")
    return sum(int(num) if num != "" else 0 for num in num_list)


cities = [
    "Paris",
    "Budapest",
    "Skopje",
    "Rotterdam",
    "Valencia",
    "Vancouver",
    "Amsterdam",
    "Vienna",
    "Sydney",
    "New York City",
    "London",
    "Bangkok",
    "Hong Kong",
    "Dubai",
    "Rome",
    "Istanbul",
]


def search_cities(str_to_search):
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
    cities_found = []

    # Requirement 5: If search text is "*", return all cities
    if str_to_search == "*":
        return cities

    # Requirement 1: If search text is fewer than 2 characters, return no results
    if len(str_to_search) < 2:
        return cities_found

    # Convert search text to lowercase for case-insensitive search (Requirement 3)
    search_lower = str_to_search.lower()

    for city in cities:
        city_lower = city.lower()
        # Requirement 2: Cities starting with search text
        # Requirement 4: Cities containing search text (substring search)
        if city_lower.startswith(search_lower) or search_lower in city_lower:
            cities_found.append(city)

    return cities_found
