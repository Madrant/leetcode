#!/usr/bin/python3

import unittest
import time

from run import Solution

class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print("%f sec" % (t))

    def test1(self):
        nums = range(100)

        ret = self.solution.containsDuplicate(nums)

        self.assertFalse(ret)

    def test2(self):
        nums = list(range(100)) + list(range(100))

        ret = self.solution.containsDuplicate(nums)

        self.assertTrue(ret)


if __name__ == "__main__":
    unittest.main()
