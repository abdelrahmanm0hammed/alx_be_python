import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc =SimpleCalculator()

    def test_add(self):
        # test the addition method

        self.assertEqual(self.calc.add(2,3),5)
    def test_subtract(self):
        #test the subtraction method
        self.assertEqual(self.calc.subtract(3,3),0)

    def test_multiply(self):
        #test the multiplication method
        self.assertEqual(self.calc.multiply(2,2),4)
    
    def test_divide(self):
        # test the division method
        self.assertEqual(self.calc.divide(2,2),1)