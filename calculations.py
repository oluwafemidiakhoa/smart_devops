import unittest

# Mock the calculations module by defining the add function here
def add(x, y):
    return x + y

class TestCalculations(unittest.TestCase):
    def test_add(self):
        # Test positive numbers
        self.assertEqual(add(3, 2), 5)

        # Test negative numbers
        self.assertEqual(add(-3, -2), -5)

        # Test positive and negative numbers
        self.assertEqual(add(3, -2), 1)

        # Test with 0
        self.assertEqual(add(0, 2), 2)

if __name__ == '__main__':
    unittest.main()
