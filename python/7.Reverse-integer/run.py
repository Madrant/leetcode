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

# Solution using a list of characters
class Solution:
    int32_min = -1 * (2 ** 31) # INT_MIN
    int32_max = (2 ** 31) - 1  # INT_MAX

    def reverse(self, n: int) -> int:
        # Convert integer to string
        # then convert string to a list of chars
        # then reverse characters order in list
        char_list = []
        char_list += str(abs(n))
        char_list.reverse()

        # Convert reversed list back t string
        # then convert string to int
        str_reversed = "".join(char_list)
        reversed_num = int(str_reversed)

        # Reverse sign of output if input value is negative
        if n < 0:
            reversed_num = reversed_num * -1

        # Check if output value fits to a signed 32-bit int boundaries
        if reversed_num < self.int32_min or reversed_num > self.int32_max:
            reversed_num = 0

        return reversed_num

# Test function
def test_solution(class_name, n, loops = 1):
    print("Solution: %s" % (class_name))
    sol = class_name()

    time = Stopwatch()

    for l in range(0, loops):
        n_reversed = sol.reverse(n)

    time.stop()

    print("Result: %i" % (n_reversed))

    time.print(loops)

    return n_reversed

# Main
if __name__ == "__main__":
    print("Arguments: %s" % (str(sys.argv)))

    if len(sys.argv) == 1:
        print("%s: <num> <loops default:1>" % (sys.argv[0]))
        sys.exit(0)

    num = int(sys.argv[1])
    loops = int(sys.argv[2]) if len(sys.argv) >= 3 is not None else 1

    print("Num: %i Loops: %u" % (num, loops))

    # Test solutions:
    n_reversed = test_solution(Solution, num, loops)
