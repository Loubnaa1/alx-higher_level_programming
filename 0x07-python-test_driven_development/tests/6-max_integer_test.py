#!/usr/bin/python3
"""
unittest to test max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Testing the max_integer function
    """
    def test_empty(self):
        """ test emty cases """
        self.assertEqual(max_integer(""), None)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_num(self):
        """testing negative and positive numbers """
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1.5, 7, 8]), 8)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([5, 6, 7]), 7)
        self.assertEqual(max_integer([1, 3, 2]), 3)
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([-1, 3, -3]), 3)

    def test_data(self):
        """testing strings """
        self.assertEqual(max_integer("loubna"), "u")
        self.assertEqual(max_integer(["mini", "ziko"]), "ziko")


if __name__ == '__main__':
    unittest.main()
