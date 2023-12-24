#!/usr/bin/python3

import unittest

from solution import Solution1, Solution2, Solution3

class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution3()

    def test1(self):
        s1 = "a"
        s2 = "a"
        answer = 0

        ret = self.solution.strStr(s1, s2)

        self.assertEqual(ret, answer)

    def test2(self):
        s1 = "abcdef"
        s2 = "def"
        answer = 3

        ret = self.solution.strStr(s1, s2)

        self.assertEqual(ret, answer)

    def test3(self):
        s1 = "sadbutsad"
        s2 = "sad"
        answer = 0

        ret = self.solution.strStr(s1, s2)

        self.assertEqual(ret, answer)

    def test4(self):
        s1 = "leetcode"
        s2 = "leeto"
        answer = -1

        ret = self.solution.strStr(s1, s2)

        self.assertEqual(ret, answer)

    def test5(self):
        s1 = "mississippi"
        s2 = "issip"
        answer = 4

        ret = self.solution.strStr(s1, s2)

        self.assertEqual(ret, answer)

    def test6(self):
        s1 = "aaaaa"
        s2 = "bba"
        answer = -1

        ret = self.solution.strStr(s1, s2)

        self.assertEqual(ret, answer)

if __name__ == "__main__":
    unittest.main()
