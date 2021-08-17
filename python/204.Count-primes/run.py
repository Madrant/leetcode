#!/usr/bin/python3

import sys
import datetime

from typing import List

from utils import Stopwatch

# Solution using a list of characters
class SolutionBase:
    max_num = 5 * (10 ** 6)

    @staticmethod
    def notPrime(n: int) -> bool:
        """ The number is definitely not a prime number """

        # 0 and 1 is not a prime numbers
        if n in {0, 1}:
            return True

        # Filter numbers divisible by some prime numbers
        #
        # Multiple if are faster than for loop in a set or list
        if n != 2 and n % 2 == 0:
            return True

        if n != 3 and n % 3 == 0:
            return True

        if n != 15 and n % 15 == 0:
            return True

        if n != 7 and n % 7 == 0:
            return True

        if n != 11 and n % 11 == 0:
            return True

        if n != 13 and n % 13 == 0:
            return True

        if n != 17 and n % 17 == 0:
            return True

        return False

    def countPrimes(self, n: int) -> int:
        """ Count prime numbers up to n """

        primes_count = 0

        for num in range(2, n):
            if self.isPrime(num):
                primes_count += 1

        return primes_count

class NaiveSolution(SolutionBase):

    def isPrime(n: int) -> bool:
        """ Check if number is a prime number """

        # Check if a number is not a prime number
        if self.notPrime(n):
            return False

        is_prime = True

        for div in range(2, n):
            if n % div == 0:
                is_prime = False
                break

        return is_prime

# Fast Solution
class FastSolution(SolutionBase):
    cache = {2, 3, 5, 7, 11, 13, 17}

    def isPrime(self, n: int) -> bool:
        """ Check if number is a prime number the fast way """

        # Check if a number is not a prime number
        if self.notPrime(n):
            return False

        # Check number is in prime numbers cache
        if n in self.cache:
            return True

        # Check if a number if divisible with a cached prime numbers
        for c in self.cache:
            if n != c and n % c == 0:
                return False

        # Check if number is prime using square root method
        s = int(n ** (1/2))

        for div in range(2, s + 1):
            # Check if div is already in prime numbers cache
            div_is_cached = div in self.cache
            if div_is_cached:
                div_is_prime = div_is_cached
            else:
                div_is_prime = self.isPrime(div)

            # Cache div if it is not cached yet
            if div_is_prime and not div_is_cached:
                self.cache.add(div)

            # Check if input number is not prime
            if div_is_prime and n % div == 0:
                return False

        # At least the number is a prime number
        return True

# Main
if __name__ == "__main__":
    print("Arguments: %s" % (str(sys.argv)))

    if len(sys.argv) == 1:
        print("%s: <num> <loops default:1>" % (sys.argv[0]))
        sys.exit(0)

    num = int(sys.argv[1])

    print(f"Num: {num}")

    # Test solutions:
    s = FastSolution()
    primes_count = s.countPrimes(num)
    print(f"Primes number for a {num}: {primes_count}")
