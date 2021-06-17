#!/usr/bin/python3

import unittest
import random

from run import Solution

class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        self.random_loops = 10000

    def test_uniform(self):
        self.assertEqual(
            self.solution.twoSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9),
            [0, 7]
        )

    def test_zero(self):
        self.assertEqual(
            self.solution.twoSum([9, 0, 2, 7], 9),
            [0, 1]
        )

    def test_repeat(self):
        self.assertEqual(
            self.solution.twoSum([3, 0, 2, 7], 9),
            [2, 3]
        )

    def test_empty(self):
        self.assertEqual(
            self.solution.twoSum([3, 0, 1, 7], 9),
            None
        )

    def test_random(self):
        for i in range(0, self.random_loops):
            # Create a random-size list of random values
            rand_nums = random.sample(range(-100, 100), random.randint(0, 100))
            rand_target = random.randint(-100, 100)

            #print("Target: %i Nums: %s" % (rand_target, str(rand_nums)))

            indices = self.solution.twoSum(rand_nums, rand_target)

            if indices is None:
                #print("No result")
                continue

            # Get values by indices
            values = [rand_nums[idx] for idx in indices]

            #print("Indices: %s Values: %s" % (str(indices), str(values)))

            # Check function result
            self.assertEqual(sum(values), rand_target)

if __name__ == "__main__":
    unittest.main()
