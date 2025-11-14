import unittest
import test

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(test.add(10, 5), 15)