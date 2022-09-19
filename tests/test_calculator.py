import unittest
import calculator
'''
Sum
* Int as input - return the int
* int + floats - return the float
* Strings as input - raise an exception

Substraction
* Int + int/floats as input - return the result
* int + floats as input - return the float
* Strings as input - raise an exception

Division
* Int as input - return the result
* int + floats as input - return the float
* Strings as input - raise an exception
* Ints/floats divided by 0 - raise ZeroDivision

Multiply
* Int/floats as input - return result
* int + floats as input - return the float
* Strings as input - raise an exception
'''


class TestCalculator(unittest.TestCase):
    def test_sum_int(self):
        self.assertEqual(10, calculator.suma(5, 5))

    def test_sum_floats(self):
        self.assertEqual(10.5, calculator.suma(5.25, 5.25))

    def test_sum_string(self):
        self.assertRaises(TypeError, calculator.suma, 5, 'string')
