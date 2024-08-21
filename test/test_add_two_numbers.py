import unittest

def add_two_numbers(a, b):
    return a + b

class TestAddTwoNumbers(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add_two_numbers(1, 2), 3)       
        self.assertEqual(add_two_numbers(-1, 1), 0)      
        self.assertEqual(add_two_numbers(-1, -1), -2)    

if __name__ == '__main__':
    unittest.main()
