import unittest

from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
	def setUp(self):
		self.calc = SimpleCalculator()

	def test_addition(self):
		self.assertEqual(self.calc.add(2, 3), 5)
		self.assertEqual(self.calc.add(-1, 1), 0)
		self.assertEqual(self.calc.add(0, 0), 0)
		self.assertAlmostEqual(self.calc.add(2.5, 0.5), 3.0)

	def test_subtraction(self):
		self.assertEqual(self.calc.subtract(5, 3), 2)
		self.assertEqual(self.calc.subtract(3, 5), -2)
		self.assertEqual(self.calc.subtract(0, 0), 0)
		self.assertAlmostEqual(self.calc.subtract(2.5, 0.5), 2.0)

	def test_multiplication(self):
		self.assertEqual(self.calc.multiply(4, 3), 12)
		self.assertEqual(self.calc.multiply(-2, 3), -6)
		self.assertEqual(self.calc.multiply(0, 100), 0)
		self.assertAlmostEqual(self.calc.multiply(2.5, 0.4), 1.0)

	def test_division_normal(self):
		self.assertEqual(self.calc.divide(10, 5), 2)
		self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
		self.assertAlmostEqual(self.calc.divide(-9, 3), -3)

	def test_division_by_zero(self):
		self.assertIsNone(self.calc.divide(10, 0))
		self.assertIsNone(self.calc.divide(0, 0))

	def test_division_edge_cases(self):
		# Very small denominator
		self.assertAlmostEqual(self.calc.divide(1e-9, 1e-9), 1.0)
		# Large numbers
		self.assertAlmostEqual(self.calc.divide(1e9, 2), 5e8)


if __name__ == "__main__":
	unittest.main()

