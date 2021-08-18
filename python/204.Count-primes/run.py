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

class FastestSolution(SolutionBase):

    # overrides SolutionBase
    def countPrimes(self, n: int, debug = False) -> int:
        """ Count prime numbers up to n """

        # An array marking sequential numbers 0 up to n as primes or not
        #
        # Skip 0 and 1 as not prime numbers
        is_primes = [True if n not in (0,1) else False for n in range(0,n)]

        # 0 and 1 is not prime numbers
#        is_primes[0] = False
#        is_primes[1] = False

        # A square root of n to iterate over
        s = int(n ** (1/2))
        if debug: print(f"s: {s}")

        # i is a sequential numbers from 2 to sqrt(n):
        #
        # for n = 20, s = 4
        #
        # i will be [2, 3, 4] -> a base to generate and mark non-prime products
        i_values = [i for i in range(2, s + 1)]

        # Alternate way to generate i values:
        # i_values = [i for i in range(2, n) if i * i < n]

        if debug: print(f"i: {i_values}")

        for i in i_values:
            # Skip values already marked as non-prime
            if is_primes[i] == False:
                continue

            # Generate j as a product of i:
            #
            # for n = 20
            #
            # for i = 2, j will be [4, 6, 8, 10, 12, 14, 16, 18] -> marked as non-primes
            # for i = 3, j will be [9, 12, 15, 18] -> marked as non-primes
            j_values = [j for j in range(i * i, n, i)]
            if debug: print(f"i: {i} j: {j_values}")

            # Mark each value with index j as non-prime
            for j in j_values:
                is_primes[j] = False

        # Count values still marked as primes
        primes_count = is_primes.count(True)

        # Show indexes, values and flags in debug mode
        if debug:
            nums = [n for n in range(0, n)]

            for i, (val, is_prime) in enumerate(zip(nums, is_primes)):
                prime_str = "Prime" if is_prime else "Not Prime"
                print(f"{i:02}: {val}: {prime_str}")

        return primes_count

# Main
if __name__ == "__main__":
    print("Arguments: %s" % (str(sys.argv)))

    if len(sys.argv) == 1:
        print("%s: <num> <loops default:1>" % (sys.argv[0]))
        sys.exit(0)

    num = int(sys.argv[1])

    print(f"Num: {num}")

    # Test solutions:
    s = FastestSolution()
    primes_count = s.countPrimes(num)
    print(f"Primes number for a {num}: {primes_count}")
