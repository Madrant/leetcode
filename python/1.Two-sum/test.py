#!/usr/bin/python3

import unittest
import random

from run import Solution, DictSolution

class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        self.random_loops = 10000

    def indices(self, nums, target):
        indices = self.solution.twoSum(nums, target)

        if indices is None:
            return []

        return indices

    def values(self, nums, target):
        indices = self.indices(nums, target)

        if indices is None:
            return []

        values = [nums[idx] for idx in indices]
        return values

    def values_sum(self, nums, target):
        return sum(self.values(nums, target))

    def test_uniform(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 9

        self.assertIsNotNone(self.indices(nums, target))
        self.assertEqual(self.values_sum(nums, target), target)

    def test_zero(self):
        nums = [9, 0, 2, 7]
        target = 9

        self.assertIsNotNone(self.indices(nums, target))
        self.assertEqual(self.values_sum(nums, target), target)

    def test_repeat(self):
        nums = [3, 0, 2, 7]
        target = 9

        self.assertIsNotNone(self.indices(nums, target))
        self.assertEqual(self.values_sum(nums, target), target)

    def test_empty(self):
        nums = [3, 0, 1, 7]
        target = 9

        self.assertIsNone(self.solution.twoSum(nums, target))

    def test_random(self):
        for i in range(0, self.random_loops):
            # Create a random-size list of random values
            rand_nums = random.sample(range(-100, 100), random.randint(0, 100))
            rand_target = random.randint(-100, 100)

            #print("Target: %i Nums: %s" % (rand_target, str(rand_nums)))

            indices = self.solution.twoSum(rand_nums, rand_target)

            if indices is None:
                continue

            # Get values by indices
            values = [rand_nums[idx] for idx in indices]

            #print("Indices: %s Values: %s" % (str(indices), str(values)))

            # Check function result
            self.assertEqual(sum(values), rand_target)

class DictSolutionTest(SolutionTest):
    def setUp(self):
        self.solution = DictSolution()
        self.random_loops = 10000

if __name__ == "__main__":
    unittest.main()
