#!/usr/bin/python3

import unittest

from run import Solution

class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test1(self):
        args = ["test", "testing", "tester"]
        answer = "test"

        ret = self.solution.longestCommonPrefix(args)

        self.assertEqual(ret, answer)

    def test2(self):
        args = ["abc", "abcd", "abcde", "abcdef"]
        answer = "abc"

        ret = self.solution.longestCommonPrefix(args)

        self.assertEqual(ret, answer)

    def test3(self):
        args = ["abcdef", "abcde", "abcde", "abcdef"]
        answer = "abcde"

        ret = self.solution.longestCommonPrefix(args)

        self.assertEqual(ret, answer)


    def test4(self):
        args = ["abc", "def", "ghi", "jkl"]
        answer = ""

        ret = self.solution.longestCommonPrefix(args)

        self.assertEqual(ret, answer)

    def test5(self):
        args = ["flower", "flow", "flight"]
        answer = "fl"

        ret = self.solution.longestCommonPrefix(args)

        self.assertEqual(ret, answer)

    def test6(self):
        args = ["a"]
        answer = "a"

        ret = self.solution.longestCommonPrefix(args)

        self.assertEqual(ret, answer)

    def test7(self):
        args = ["ab", "a"]
        answer = "a"

        ret = self.solution.longestCommonPrefix(args)

        self.assertEqual(ret, answer)


if __name__ == "__main__":
    unittest.main()
