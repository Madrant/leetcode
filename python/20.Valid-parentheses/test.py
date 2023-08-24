#!/usr/bin/python3

import unittest

from run import Solution

class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test1(self):
        args = "()"
        answer = True

        ret = self.solution.isValid(args)

        self.assertEqual(ret, answer)

    def test2(self):
        args = "()[]{}"
        answer = True

        ret = self.solution.isValid(args)

        self.assertEqual(ret, answer)

    def test3(self):
        args = "(]"
        answer = False

        ret = self.solution.isValid(args)

        self.assertEqual(ret, answer)

    def test4(self):
        args = "{[]}"
        answer = True

        ret = self.solution.isValid(args)

        self.assertEqual(ret, answer)

    def test5(self):
        args = "{][}"
        answer = False

        ret = self.solution.isValid(args)

        self.assertEqual(ret, answer)

    def test6(self):
        args = "{[}]"
        answer = False

        ret = self.solution.isValid(args)

        self.assertEqual(ret, answer)

    def test7(self):
        args = "{"
        answer = False

        ret = self.solution.isValid(args)

        self.assertEqual(ret, answer)

    def test8(self):
        args = "]]"
        answer = False

        ret = self.solution.isValid(args)

        self.assertEqual(ret, answer)

if __name__ == "__main__":
    unittest.main()
