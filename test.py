import check
import unittest
class TestStringMethods(unittest.TestCase):
	def test_sum(self):
		self.assertEqual(sum([1,2,3]),6)
	def test_sumZero(self):
		self.assertEqual(sum([0,0,0]),0)
	def test_sumNull(self):
		self.assertEqual(sum([]),0)
	def test_sumInt(self):
		self.assertEqual(sum([1]),1)
	def test_sumFloat(self):
		self.assertEqual(sum([1.0, 3.0]),4)
if __name__ == '__main__':
    unittest.main()