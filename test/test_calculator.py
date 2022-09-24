import unittest
import calculator

'''
Sum
* Int as input - return the int
* Strings as input - raise an exception

Substraction
* Int as input - return the result
* Strings as input - raise an exception

Division
* Int/floats as input - return the result
* Strings as input - raise an exception
* Ints/floats divided by 0 - raise ZeroDivision
--
Multiply
* Int/floats as input - return result
* Strings as input - raise an exception
'''


class TestCalculator(unittest.TestCase):
    # Sum Test
    def test_sum_int(self):
        self.assertEqual(10, calculator.suma(5, 5))

    # Substract Test
    def test_substract_int(self):
        self.assertEqual(10, calculator.substract(20, 10))

    # Division Tests
    def test_divide_int(self):
        self.assertEqual(10, calculator.substract(20, 10))

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, calculator.divide, 5, 0)

    # Multiply Test
    def test_multiply(self):
        self.assertEqual(30, calculator.multiply(6, 5))

