#!/usr/bin/python3

import unittest

from run import Solution

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test1(self):
        nums = [1, 2, 2, 3, 3]
        answer = 1

        ret = self.solution.singleNumber(nums)

        self.assertEqual(ret, answer)

    def test1(self):
        nums = [1, 2, 2, 3, 3, 1, 5]
        answer = 5

        ret = self.solution.singleNumber(nums)

        self.assertEqual(ret, answer)

if __name__ == "__main__":
    unittest.main()
