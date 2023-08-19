#!/usr/bin/python3

import unittest

from run import Solution

class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test1(self):
        roman = "III"
        answer = 3

        ret = self.solution.romanToInt(roman)

        self.assertEqual(ret, answer)

    def test2(self):
        roman = "IV"
        answer = 4

        ret = self.solution.romanToInt(roman)

        self.assertEqual(ret, answer)

    def test3(self):
        roman = "MCDLXXVI"
        answer = 1476

        ret = self.solution.romanToInt(roman)

        self.assertEqual(ret, answer)

if __name__ == "__main__":
    unittest.main()