#!/usr/bin/python3

import unittest

from run import NaiveSolution, FastSolution, FastestSolution

class SolutionTest(unittest.TestCase):

    def setUp(self):
        self.solution = None

    def test_2_countPrimes(self):
        if not self.solution:
            return

        self.assertEqual(self.solution.countPrimes(0), 0)
        self.assertEqual(self.solution.countPrimes(1), 0)
        self.assertEqual(self.solution.countPrimes(2), 0)
        self.assertEqual(self.solution.countPrimes(3), 1)
        self.assertEqual(self.solution.countPrimes(4), 2)
        self.assertEqual(self.solution.countPrimes(5), 2)
        self.assertEqual(self.solution.countPrimes(6), 3)
        self.assertEqual(self.solution.countPrimes(7), 3)
        self.assertEqual(self.solution.countPrimes(8), 4)
        self.assertEqual(self.solution.countPrimes(9), 4)
        self.assertEqual(self.solution.countPrimes(10), 4)

        # There are 500 prime numbers before 3572
        self.assertEqual(self.solution.countPrimes(3572), 500)

class NaiveSolutionTest(SolutionTest):

    def setUp(self):
        self.solution = NaiveSolution()

    def test_1_isPrime(self):
        return
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

class NaiveSolutionTest(NaiveSolutionTest):

    def setUp(self):
        self.solution = FastSolution()

class FastestSolutionTest(SolutionTest):

    def setUp(self):
        self.solution = FastestSolution()

if __name__ == "__main__":
    unittest.main(verbosity = 2)
