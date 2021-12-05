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


class TestFrac(unittest.TestCase):

    def test_simple_fraction_as_strings(self):
        actual = Frac('a + b', 'c + d')
        self.assertEqual(r'\frac{a + b}{c + d}', actual)

    def test_simple_fraction_as_symbols(self):
        actual = Frac(a+b, c+d)
        self.assertEqual(r'\frac{a + b}{c + d}', actual)


class TestSqrt(unittest.TestCase):

    def test_sqrt_with_str_arg(self):
        actual = Sqrt('b^2 - 4ac')
        self.assertEqual(r'\sqrt{b^2 - 4ac}', actual)

    def test_sqrt_with_symbol_arg(self):
        actual = Sqrt(b**2 - 4 * a * c)
        self.assertEqual(r'\sqrt{b^2 - 4 a c}', actual)


class TestTagging(unittest.TestCase):

    def test_tag_and_retrieve_subexpression(self):
        Frac(-b + Sqrt(b**2 - 4*a*c, tag='the_root'), 2*a)
        actual = get('the_root')
        self.assertEqual(str(Sqrt(b**2 - 4*a*c)), actual)



