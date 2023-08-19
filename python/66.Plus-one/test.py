#!/usr/bin/python3

import unittest

from run import Solution

class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test1(self):
        digits = [1, 2, 3]
        answer = [1, 2, 4]

        ret = self.solution.plusOne(digits)
        self.assertEqual(ret, answer)

    def test2(self):
        digits = [0]
        answer = [1]

        ret = self.solution.plusOne(digits)
        self.assertEqual(ret, answer)

    def test3(self):
        digits = [9]
        answer = [1, 0]

        ret = self.solution.plusOne(digits)
        self.assertEqual(ret, answer)

    def test4(self):
        digits = [9, 9]
        answer = [1, 0, 0]

        ret = self.solution.plusOne(digits)
        self.assertEqual(ret, answer)

if __name__ == "__main__":
    unittest.main()
