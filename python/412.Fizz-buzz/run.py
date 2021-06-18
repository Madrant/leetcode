#!/usr/bin/python3

import sys
import datetime

from typing import List

# Class to perform time measurements
class Stopwatch:
    def __init__(self):
        self.start = datetime.datetime.now()

    def stop(self):
        self.stop = datetime.datetime.now()
        self.time = self.stop - self.start

    def print(self, loops = 1):
        step_time = self.time / loops
        print(
            "%sime: %u sec %u usec" %
            ("Loops: %i Time: %u sec %u usec Step t" %
            (loops, self.time.seconds, self.time.microseconds) if loops > 1 else "T",
            step_time.seconds, step_time.microseconds)
        )

# Straightforward solution
class Solution:

    def fizzBuzz(self, n: int) -> List[str]:
        strings = []

        for i in range(1, n + 1):

            div_by_3 = (i % 3 == 0)
            div_by_5 = (i % 5 == 0)

            if div_by_3 and div_by_5:
                strings += ["FizzBuzz"]

            elif div_by_3:
                strings += ["Fizz"]

            elif div_by_5:
                strings += ["Buzz"]

            else:
                strings += [str(i)]

        return strings

# More complex if
class Solution2:
    fizz = "Fizz"
    buzz = "Buzz"

    def fizzBuzz(self, n: int) -> List[str]:
        strings = []

        for i in range(1, n + 1):

            if i % 3 == 0:

                if i % 5 == 0:
                    strings += [self.fizz + self.buzz]
                else:
                    strings += [self.fizz]

            elif i % 5 == 0:
                strings += [self.buzz]

            else:
                strings += [str(i)]

        return strings

# String concatenation
class Solution3:
    fizz = "Fizz"
    buzz = "Buzz"

    def fizzBuzz(self, n: int) -> List[str]:
        strings = []

        for i in range(1, n + 1):

            if i % 3 == 0:
                strings += [self.fizz]

                if i % 5 == 0:
                    strings[-1] += self.buzz

            elif i % 5 == 0:
                strings += [self.buzz]

            else:
                strings += [str(i)]

        return strings

# Hash
class Solution4:
    fizz_dict = { 3 : "Fizz", 5 : "Buzz" }

    def fizzBuzz(self, n: int) -> List[str]:
        strings = []

        for i in range(1, n + 1):

            string = ""

            for key in self.fizz_dict.keys():
                if i % key == 0:
                    string += self.fizz_dict[key]

            if not string:
                string = str(i)

            strings.append(string)

        return strings

# Test function
def test_solution(class_name, n, loops = 1000):
    print("Solution: %s" % (class_name))
    sol = class_name()

    time = Stopwatch()

    for l in range(0, loops):
        strings = sol.fizzBuzz(n)

    time.stop()

    if strings is None:
        print("No result")
        return

    print("Result: Strings: %s" % (str(strings)))

    time.print(loops)

    return strings

# Main
if __name__ == "__main__":
    print("Arguments: %s" % (str(sys.argv)))

    if len(sys.argv) == 1:
        print("%s: <num> <loops default:1>" % (sys.argv[0]))
        sys.exit(0)

    num = int(sys.argv[1])
    loops = int(sys.argv[2]) if len(sys.argv) else 1

    print("Num: %i Loops: %u" % (num, loops))

    # Test solutions:
    strings1 = test_solution(Solution, num, loops)
    strings2 = test_solution(Solution2, num, loops)
    strings3 = test_solution(Solution3, num, loops)
    strings4 = test_solution(Solution4, num, loops)

    assert(strings1 == strings2)
    assert(strings1 == strings3)
    assert(strings1 == strings4)
