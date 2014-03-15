import unittest
from discount_calculator import DiscountCalculator

class test_DiscountCalculator(unittest.TestCase):
	def setUp(self):
		self.dc = DiscountCalculator()

	def test_10_percent(self):
		r = self.dc.calculate_discount(100, 10, "%")
		self.assertEquals(10.0, r)
	
	def test_101_percent(self):
		self.assertRaises(ValueError, self.dc.calculate_discount, 100, 101, "%")
	
	def test_5_dollars(self):
		r = self.dc.calculate_discount(250, 5, "$")
		self.assertEquals(245, r)
	
	def test_discount_greaterthan_dollars(self):
		self.assertRaises(ValueError, self.dc.calculate_discount, 100, 101, "$")

	def test_discount_type(self):
		self.assertRaises(ValueError, self.dc.calculate_discount, 250, 5, "test")

	def test_floating_point_type(self):
		r = self.dc.calculate_discount(100.0,10.0,'%')
		self.assertEqual(10.0, r)