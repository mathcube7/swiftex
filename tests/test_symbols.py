import unittest

from swiftex import symbols
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
        actual = a**2

        # Assert
        self.assertEqual('a^{2}', str(actual))

    def test_adding_symbols(self):
        # Arrange
        a, b = symbols('a, b')

        # Act
        actual = a**2 + b**2

        # Assert
        self.assertEqual('a^{2} + b^{2}', str(actual))

    def test_pythagoras(self):
        # Arrange
        a, b, c = symbols('a, b, c')

        # Act
        actual = a ** 2 + b ** 2 == c**2

        # Assert
        self.assertEqual('a^{2} + b^{2} = c^{2}', str(actual))

    def test_abc(self):

        # Act
        actual = x ** 2 + y ** 2 == z ** 2

        # Assert
        self.assertEqual('x^{2} + y^{2} = z^{2}', str(actual))
