# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from white_box.class_exercises import (
    VendingMachine,
    divide,
    get_grade,
    is_even,
    is_triangle,
    check_number_status,
    validate_password,
    calculate_total_discount,
    calculate_order_total,
    calculate_items_shipping_cost,
    validate_login,
    verify_age,
    categorize_product,
    validate_email,
    celsius_to_fahrenheit,
    validate_credit_card,
    validate_date,
    check_flight_eligibility,
    validate_url,
    calculate_quantity_discount,
    check_file_size,
    check_loan_eligibility,
    calculate_shipping_cost,
    grade_quiz,
    authenticate_user,
    get_weather_advisory,
)


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """

    # General helpers
    def test_is_even_with_even_number(self):
        """
        Checks if a number is even.
        """
        self.assertTrue(is_even(0))

    def test_is_even_with_odd_number(self):
        """
        Checks if a number is not even.
        """
        self.assertFalse(is_even(7))

    # divide
    def test_divide_by_non_zero(self):
        """
        Checks the divide function works as expected.
        """
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        """
        Checks the divide function returns 0 when dividing by 0.
        """
        self.assertEqual(divide(10, 0), 0)

    # get_grade
    def test_get_grade_a(self):
        """
        Checks A grade.
        """
        self.assertEqual(get_grade(95), "A")

    def test_get_grade_b(self):
        """
        Checks B grade.
        """
        self.assertEqual(get_grade(85), "B")

    def test_get_grade_c(self):
        """
        Checks C grade.
        """
        self.assertEqual(get_grade(75), "C")

    def test_get_grade_f(self):
        """
        Checks F grade.
        """
        self.assertEqual(get_grade(65), "F")

    def test_is_triangle_yes(self):
        """
        Checks the three inputs can form a triangle.
        """
        self.assertEqual(is_triangle(3, 4, 5), "Yes, it's a triangle!")

    def test_is_triangle_no_1(self):
        """
        Checks the three inputs can't form a triangle when C is greater or equal than A + B.
        """
        self.assertEqual(is_triangle(3, 4, 7), "No, it's not a triangle.")

    # 1 check_number_status
    def test_check_number_status_positive(self):
        self.assertEqual(check_number_status(5), "Positive")

    def test_check_number_status_negative(self):
        self.assertEqual(check_number_status(-2), "Negative")

    def test_check_number_status_zero(self):
        self.assertEqual(check_number_status(0), "Zero")

    def test_check_number_status_float(self):
        self.assertEqual(check_number_status(0.0), "Zero")

    # 2 validate_password
    def test_validate_password_too_short(self):
        self.assertFalse(validate_password("Aa1!a"))

    def test_validate_password_missing_requirements(self):
        self.assertFalse(validate_password("aaaaaaaa"))

    def test_validate_password_valid(self):
        self.assertTrue(validate_password("Abcde1!f"))

    def test_validate_password_missing_uppercase(self):
        self.assertFalse(validate_password("abcde1!f"))

    def test_validate_password_missing_lowercase(self):
        self.assertFalse(validate_password("ABCDE1!F"))

    def test_validate_password_missing_digit(self):
        self.assertFalse(validate_password("Abcdef!g"))

    def test_validate_password_missing_special(self):
        self.assertFalse(validate_password("Abcde12f"))

    def test_validate_password_length_boundary(self):
        self.assertTrue(validate_password("A1bcd!ef"))

    # 3 calculate_total_discount
    def test_calculate_total_discount_none(self):
        self.assertEqual(calculate_total_discount(50), 0)

    def test_calculate_total_discount_ten_percent(self):
        self.assertEqual(calculate_total_discount(200), 20.0)

    def test_calculate_total_discount_twenty_percent(self):
        self.assertEqual(calculate_total_discount(600), 120.0)

    def test_calculate_total_discount_at_100(self):
        self.assertEqual(calculate_total_discount(100), 10.0)

    def test_calculate_total_discount_at_500(self):
        self.assertEqual(calculate_total_discount(500), 50.0)

    # 4 calculate_order_total
    def test_calculate_order_total_various_discounts(self):
        items = [
            {"quantity": 3, "price": 10},
            {"quantity": 6, "price": 5},
            {"quantity": 12, "price": 2},
        ]
        self.assertAlmostEqual(calculate_order_total(items), 80.1)

    def test_calculate_order_total_boundaries(self):
        items = [{"quantity": 5, "price": 10}, {"quantity": 6, "price": 10}]
        self.assertAlmostEqual(calculate_order_total(items), 107)

    # 5 calculate_items_shipping_cost
    def test_calculate_items_shipping_cost_standard(self):
        items = [{"weight": 2}, {"weight": 2}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_calculate_items_shipping_cost_express(self):
        items = [{"weight": 6}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_calculate_items_shipping_cost_invalid_method(self):
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost([{"weight": 1}], "overnight")

    def test_calculate_items_shipping_cost_weight_boundaries(self):
        self.assertEqual(calculate_items_shipping_cost([{"weight": 5}], "standard"), 10)
        self.assertEqual(calculate_items_shipping_cost([{"weight": 5}], "express"), 20)
        self.assertEqual(calculate_items_shipping_cost([{"weight": 10}], "standard"), 15)
        self.assertEqual(calculate_items_shipping_cost([{"weight": 10}], "express"), 30)

    # 6 validate_login
    def test_validate_login_success(self):
        self.assertEqual(validate_login("usuario", "password"), "Login Successful")

    def test_validate_login_failed(self):
        self.assertEqual(validate_login("usr", "pwd"), "Login Failed")

    def test_validate_login_length_boundaries(self):
        self.assertEqual(validate_login("user5", "passwrd8"), "Login Successful")
        self.assertEqual(validate_login("u" * 20, "p" * 15), "Login Successful")

    # 7 verify_age
    def test_verify_age_eligible(self):
        self.assertEqual(verify_age(30), "Eligible")

    def test_verify_age_not_eligible(self):
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_verify_age_boundaries(self):
        self.assertEqual(verify_age(18), "Eligible")
        self.assertEqual(verify_age(65), "Eligible")
        self.assertEqual(verify_age(66), "Not Eligible")

    # 8 categorize_product
    def test_categorize_product(self):
        self.assertEqual(categorize_product(25), "Category A")
        self.assertEqual(categorize_product(75), "Category B")
        self.assertEqual(categorize_product(150), "Category C")
        self.assertEqual(categorize_product(5), "Category D")

    def test_categorize_product_boundaries(self):
        self.assertEqual(categorize_product(10), "Category A")
        self.assertEqual(categorize_product(50), "Category A")
        self.assertEqual(categorize_product(51), "Category B")
        self.assertEqual(categorize_product(100), "Category B")
        self.assertEqual(categorize_product(101), "Category C")
        self.assertEqual(categorize_product(200), "Category C")

    # 9 validate_email
    def test_validate_email_valid(self):
        self.assertEqual(validate_email("user@example.com"), "Valid Email")

    def test_validate_email_invalid(self):
        self.assertEqual(validate_email("useratexample"), "Invalid Email")

    def test_validate_email_min_length(self):
        self.assertEqual(validate_email("a@b.c"), "Valid Email")

    def test_validate_email_missing_dot(self):
        self.assertEqual(validate_email("user@domain"), "Invalid Email")

    # 10 celsius_to_fahrenheit
    def test_celsius_to_fahrenheit_valid(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_celsius_to_fahrenheit_invalid(self):
        self.assertEqual(celsius_to_fahrenheit(200), "Invalid Temperature")

    def test_celsius_to_fahrenheit_boundaries(self):
        self.assertEqual(celsius_to_fahrenheit(-100), -148.0)
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)

    # 11 validate_credit_card
    def test_validate_credit_card_valid(self):
        self.assertEqual(validate_credit_card("4111111111111"), "Valid Card")

    def test_validate_credit_card_invalid(self):
        self.assertEqual(validate_credit_card("abcd"), "Invalid Card")

    def test_validate_credit_card_length_boundaries(self):
        self.assertEqual(validate_credit_card("1" * 13), "Valid Card")
        self.assertEqual(validate_credit_card("1" * 16), "Valid Card")

    # 12 validate_date
    def test_validate_date_valid(self):
        self.assertEqual(validate_date(2020, 12, 15), "Valid Date")

    def test_validate_date_invalid(self):
        self.assertEqual(validate_date(1800, 1, 1), "Invalid Date")

    def test_validate_date_year_boundaries(self):
        self.assertEqual(validate_date(1900, 1, 1), "Valid Date")
        self.assertEqual(validate_date(2100, 12, 31), "Valid Date")

    # 13 check_flight_eligibility
    def test_check_flight_eligibility_by_age(self):
        self.assertEqual(check_flight_eligibility(30, False), "Eligible to Book")

    def test_check_flight_eligibility_by_ff(self):
        self.assertEqual(check_flight_eligibility(16, True), "Eligible to Book")

    def test_check_flight_eligibility_boundaries(self):
        self.assertEqual(check_flight_eligibility(18, False), "Eligible to Book")
        self.assertEqual(check_flight_eligibility(65, False), "Eligible to Book")

    # 14 validate_url
    def test_validate_url_valid(self):
        self.assertEqual(validate_url("http://example.com"), "Valid URL")

    def test_validate_url_invalid(self):
        self.assertEqual(validate_url("ftp://example.com"), "Invalid URL")

    def test_validate_url_https_long(self):
        long_https = "https://" + "a" * 300
        self.assertEqual(validate_url(long_https), "Valid URL")

    def test_validate_url_http_too_long(self):
        long_http = "http://" + "a" * 300
        self.assertEqual(validate_url(long_http), "Invalid URL")

    # 15 calculate_quantity_discount
    def test_calculate_quantity_discount(self):
        self.assertEqual(calculate_quantity_discount(3), "No Discount")
        self.assertEqual(calculate_quantity_discount(7), "5% Discount")
        self.assertEqual(calculate_quantity_discount(20), "10% Discount")

    def test_calculate_quantity_discount_boundaries(self):
        self.assertEqual(calculate_quantity_discount(1), "No Discount")
        self.assertEqual(calculate_quantity_discount(5), "No Discount")
        self.assertEqual(calculate_quantity_discount(6), "5% Discount")
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")

    # 16 check_file_size
    def test_check_file_size_valid(self):
        self.assertEqual(check_file_size(500000), "Valid File Size")

    def test_check_file_size_invalid(self):
        self.assertEqual(check_file_size(2000000), "Invalid File Size")

    def test_check_file_size_boundaries(self):
        self.assertEqual(check_file_size(0), "Valid File Size")
        self.assertEqual(check_file_size(1048576), "Valid File Size")
        self.assertEqual(check_file_size(-1), "Invalid File Size")

    # 17 check_loan_eligibility
    def test_check_loan_eligibility_not_eligible(self):
        self.assertEqual(check_loan_eligibility(20000, 600), "Not Eligible")

    def test_check_loan_eligibility_standard_vs_secured(self):
        self.assertEqual(check_loan_eligibility(40000, 710), "Standard Loan")
        self.assertEqual(check_loan_eligibility(40000, 600), "Secured Loan")

    def test_check_loan_eligibility_premium(self):
        self.assertEqual(check_loan_eligibility(80000, 760), "Premium Loan")

    def test_check_loan_eligibility_credit_boundaries(self):
        self.assertEqual(check_loan_eligibility(30000, 701), "Standard Loan")
        self.assertEqual(check_loan_eligibility(30000, 700), "Secured Loan")
        self.assertEqual(check_loan_eligibility(60000, 701), "Standard Loan")

    # 18 calculate_shipping_cost
    def test_calculate_shipping_cost_small(self):
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)

    def test_calculate_shipping_cost_medium(self):
        self.assertEqual(calculate_shipping_cost(2, 20, 20, 20), 10)

    def test_calculate_shipping_cost_large(self):
        self.assertEqual(calculate_shipping_cost(10, 50, 50, 50), 20)

    def test_calculate_shipping_cost_edge_dimensions(self):
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)
        self.assertEqual(calculate_shipping_cost(1.5, 11, 11, 11), 10)

    # 19 grade_quiz
    def test_grade_quiz_pass(self):
        self.assertEqual(grade_quiz(8, 2), "Pass")

    def test_grade_quiz_conditional(self):
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")

    def test_grade_quiz_fail(self):
        self.assertEqual(grade_quiz(3, 5), "Fail")

    def test_grade_quiz_boundaries(self):
        self.assertEqual(grade_quiz(7, 2), "Pass")
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")
        self.assertEqual(grade_quiz(4, 4), "Fail")

    # 20 authenticate_user
    def test_authenticate_user_admin(self):
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_authenticate_user_user(self):
        self.assertEqual(authenticate_user("user1", "longpass"), "User")

    def test_authenticate_user_invalid(self):
        self.assertEqual(authenticate_user("u", "p"), "Invalid")

    def test_authenticate_user_length_boundaries(self):
        self.assertEqual(authenticate_user("user5", "passwrd8"), "User")

    # 21 get_weather_advisory
    def test_get_weather_advisory_hot_and_humid(self):
        self.assertEqual(
            get_weather_advisory(35, 80), "High Temperature and Humidity. Stay Hydrated."
        )

    def test_get_weather_advisory_cold(self):
        self.assertEqual(get_weather_advisory(-5, 30), "Low Temperature. Bundle Up!")

    def test_get_weather_advisory_none(self):
        self.assertEqual(get_weather_advisory(20, 40), "No Specific Advisory")

    def test_get_weather_advisory_edge(self):
        self.assertEqual(get_weather_advisory(30, 80), "No Specific Advisory")


class TestWhiteBoxVendingMachine(unittest.TestCase):
    """
    Vending Machine unit tests.
    """

    # @classmethod
    # def setUpClass(cls):
    #    return

    def setUp(self):
        self.vending_machine = VendingMachine()
        self.assertEqual(self.vending_machine.state, "Ready")

    # def tearDown(self):
    #    return

    # @classmethod
    # def tearDownClass(cls):
    #    return

    def test_vending_machine_insert_coin_error(self):
        """
        Checks the vending machine can accept coins.
        """
        self.vending_machine.state = "Dispensing"

        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Invalid operation in current state.")

    def test_vending_machine_insert_coin_success(self):
        """
        Checks the vending machine fails to accept coins when it's not ready.
        """
        output = self.vending_machine.insert_coin()

        self.assertEqual(self.vending_machine.state, "Dispensing")
        self.assertEqual(output, "Coin Inserted. Select your drink.")


if __name__ == "__main__":
    unittest.main()
