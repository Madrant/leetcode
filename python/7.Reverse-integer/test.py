#!/usr/bin/python3

import unittest
import random

from run import Solution

class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        self.random_loops = 10000

    def test_basic(self):
        self.assertEqual(self.solution.reverse(123), 321)

    def test_negative(self):
        self.assertEqual(self.solution.reverse(-123), -321)

    def test_zero(self):
        self.assertEqual(self.solution.reverse(0), 0)

    def test_less_int_min(self):
        self.assertEqual(self.solution.reverse(self.solution.int32_min), 0)

    def test_more_int_max(self):
        self.assertEqual(self.solution.reverse(self.solution.int32_max), 0)

    def test_int_min(self):
        self.assertEqual(self.solution.reverse(7463847412), self.solution.int32_max)

    def test_int_min(self):
        self.assertEqual(self.solution.reverse(-8463847412), self.solution.int32_min)

if __name__ == "__main__":
    unittest.main()
