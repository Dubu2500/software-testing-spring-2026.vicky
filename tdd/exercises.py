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
    """
    if numbers == "":
        return 0

    num_list = numbers.split(",")
    if len(num_list) == 1:
        return int(num_list[0])

    return int(num_list[0]) + int(num_list[1])
