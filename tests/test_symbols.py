import unittest

from swiftex import *
from swiftex.abc import *


class TestSymbols(unittest.TestCase):

    def test_create_single_symbol_assigns_string(self):
        a = symbols('a')
        expected = 'a'
        actual = str(a)
        self.assertEqual(expected, actual)

    def test_create_multiple_symbols(self):
        b, c = symbols('b, c')
        self.assertEqual('b', str(b))
        self.assertEqual('c', str(c))

    def test_symbol_raised_to_power(self):
        # Arrange
        a = symbols('a')

        # Act
        actual = a ** 2

        # Assert
        self.assertEqual('a^{2}', str(actual))

    def test_adding_symbols(self):
        # Arrange
        a, b = symbols('a, b')

        # Act
        actual = a ** 2 + b ** 2

        # Assert
        self.assertEqual('a^{2} + b^{2}', str(actual))

    def test_pythagoras(self):
        # Arrange
        a, b, c = symbols('a, b, c')

        # Act
        actual = a ** 2 + b ** 2 == c ** 2

        # Assert
        self.assertEqual('a^{2} + b^{2} = c^{2}', str(actual))

    def test_abc(self):
        # Act
        actual = x ** 2 + y ** 2 == z ** 2

        # Assert
        self.assertEqual('x^{2} + y^{2} = z^{2}', str(actual))

    def test_attach_symbols(self):

        actual = a * b * c
        self.assertEqual('a b c', str(actual))


class TestIntegral(unittest.TestCase):

    def test_integral_sign_with_limits(self):
        expr = Int(-oo, oo)
        self.assertEqual(r'\int_{-\infty}^{\infty}', expr)

    def test_integral_x_squared_dx(self):
        expr = Int(a, b) * x**2 * dx
        self.assertEqual(r'\int_{a}^{b} x^{2} dx', expr)

    def test_integral_f_of_x(self):
        expr = Int(a, b) * f(x) * dx
        self.assertEqual(r'\int_{a}^{b} f \left( x \right) ^{2} dx', expr)

    def test_integral_f_of_x_and_y(self):
        expr = Int(a, b) * f(x, y) * dx
        self.assertEqual(r'\int_{a}^{b} f \left( x, y \right) ^{2} dx', expr)

    def test_integral_only_upper_limit(self):
        expr = Int('', b) * f(x, y) * dx
        self.assertEqual(r'\int_{}^{b} f \left( x, y \right) ^{2} dx', expr)

    def test_integral_only_lower_limit(self):
        expr = Int(a, '') * f(x, y) * dx
        self.assertEqual(r'\int_{}^{} f \left( x, y \right) ^{2} dx', expr)

    def test_integral_no_limits(self):
        expr = Int() * f(x, y) * dx
        self.assertEqual(r'\int f \left( x, y \right) ^{2} dx', expr)