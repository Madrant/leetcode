#!/usr/bin/python3

import unittest

from run import Solution

class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test1(self):
        args = [ 1, 1, 2]
        answer = 2

        ret = self.solution.removeDuplicates(args)

        self.assertEqual(ret, answer)

    def test2(self):
        args = [ 0, 1, 2, 3, 4]
        answer = 5

        ret = self.solution.removeDuplicates(args)

        self.assertEqual(ret, answer)

    def test3(self):
        args = [ 0, 1, 1, 2, 3, 3, 4, 4]
        answer = 5

        ret = self.solution.removeDuplicates(args)

        self.assertEqual(ret, answer)

if __name__ == "__main__":
    unittest.main()
