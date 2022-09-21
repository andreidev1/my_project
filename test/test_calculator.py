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


class TestSumCalculator(unittest.TestCase):
    def test_sum_int(self):
        self.assertEqual(10, calculator.suma(5, 5))

    def test_sum_float(self):
        self.assertEqual(10.5, calculator.suma(5.25, 5.25))

    def test_sum_string(self):
        self.assertRaises(TypeError, calculator.suma, 5, 'string')






