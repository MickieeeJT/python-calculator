import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)  # Positive integers
        self.assertEqual(self.calc.add(-1, 5), 4)  # Negative and positive integer

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)  # Simple subtraction
        self.assertEqual(self.calc.subtract(-3, 5), -8)  # Negative and positive subtraction

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)  # Positive integers
        self.assertEqual(self.calc.multiply(0, 5), 0)  # Multiplication with zero

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)  # Positive integers
        self.assertRaises(ValueError, self.calc.divide, 5, 0)  # Division by zero

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)  # Positive integers
        self.assertRaises(ValueError, self.calc.modulo, 10, 0)  # Modulo by zero

if __name__ == '__main__':
    unittest.main()
