#!/usr/bin/python3
"""Unittest for max_integer([...])"""
import unittest
from max_integer import max_integer

class TextMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertIsNone(max_integer([]))

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([-1, -1, -1, -1]), -1)

        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        self.assertEqual(max_integer([-1, -2, -3, 4]), 4)

        self.assertEqual(max_integer([42]), 42)
        self.assertEqual(max_integer([-42]), -42)

        self.assertEqual(max_integer([1, 2, 3, 4, 4]), 4)
        self.assertEqual(max_integer([4, 4, 3, 2, 1]), 4)

if __name__ == '__main__':
    unittest.main()
