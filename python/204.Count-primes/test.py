#!/usr/bin/python3

import unittest

from run import FastSolution as Solution

class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_1_isPrime(self):
        # 0 and 1 is not a prime numbers
        self.assertFalse(self.solution.isPrime(0))
        self.assertFalse(self.solution.isPrime(1))

        self.assertTrue(self.solution.isPrime(2))
        self.assertTrue(self.solution.isPrime(3))
        self.assertTrue(self.solution.isPrime(5))
        self.assertTrue(self.solution.isPrime(7))
        self.assertTrue(self.solution.isPrime(11))

        self.assertFalse(self.solution.isPrime(4))
        self.assertFalse(self.solution.isPrime(6))
        self.assertFalse(self.solution.isPrime(8))
        self.assertFalse(self.solution.isPrime(9))
        self.assertFalse(self.solution.isPrime(10))

        self.assertFalse(self.solution.isPrime(90))
        self.assertFalse(self.solution.isPrime(91))

        self.assertTrue(self.solution.isPrime(97))
        self.assertTrue(self.solution.isPrime(101))

        self.assertTrue(self.solution.isPrime(3571))

    def test_2_countPrimes(self):
        self.assertEqual(self.solution.countPrimes(0), 0)
        self.assertEqual(self.solution.countPrimes(1), 0)
        self.assertEqual(self.solution.countPrimes(10), 4)

        # There are 500 prime numbers before 3572
        self.assertEqual(self.solution.countPrimes(3572), 500)

if __name__ == "__main__":
    unittest.main()
