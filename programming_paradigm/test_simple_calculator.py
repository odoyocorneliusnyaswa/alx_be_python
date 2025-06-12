import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test cases for SimpleCalculator class"""
    
    def setUp(self):
        """Set up the SimpleCalculator instance before each test"""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        """Test the add method with various inputs"""
        # Test positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, -1), -2)
        # Test mixed positive/negative
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Test with zero
        self.assertEqual(self.calc.add(0, 5), 5)
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=7)
    
    def test_subtraction(self):
        """Test the subtract method with various inputs"""
        # Test positive numbers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        # Test negative numbers
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        # Test mixed positive/negative
        self.assertEqual(self.calc.subtract(1, -1), 2)
        # Test with zero
        self.assertEqual(self.calc.subtract(0, 5), -5)
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2, places=7)
    
    def test_multiplication(self):
        """Test the multiply method with various inputs"""
        # Test positive numbers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        # Test with zero
        self.assertEqual(self.calc.multiply(0, 5), 0)
        # Test identity
        self.assertEqual(self.calc.multiply(1, 5), 5)
        # Test floating point numbers
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.2), 0.02, places=7)
    
    def test_division(self):
        """Test the divide method with various inputs"""
        # Test normal division
        self.assertEqual(self.calc.divide(6, 3), 2)
        # Test floating point result
        self.assertAlmostEqual(self.calc.divide(1, 2), 0.5, places=7)
        # Test negative numbers
        self.assertEqual(self.calc.divide(-6, 3), -2)
        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))
        # Test zero divided by number
        self.assertEqual(self.calc.divide(0, 5), 0)
    
    def test_division_precision(self):
        """Test division with precise floating point results"""
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333, places=7)
        self.assertAlmostEqual(self.calc.divide(10, 3), 3.3333333, places=7)

if __name__ == '__main__':
    unittest.main()
