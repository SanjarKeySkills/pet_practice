import unittest
import test

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(test.add(10, 5), 15)
        self.assertEqual(test.add(-1, 1), 0)
        self.assertEqual(test.add(10, 9), 19)

    def test_add(self):
        self.assertEqual(test.add(10, 5), 15)
        self.assertEqual(test.add(-1, 1), 0)
        self.assertEqual(test.add(10, 9), 19)
        
    def test_add(self):
	    self.assertEqual(test.add(10, 5), 15)
        self.assertEqual(test.add(-1, 1), 0)
        self.assertEqual(test.add(10, 9), 19)
        
    def test_add(self):
	    self.assertEqual(test.add(10, 5), 15)
        self.assertEqual(test.add(-1, 1), 0)
        self.assertEqual(test.add(10, 9), 19)

if __name__ == '__main__':
    unittest.main()