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

    def print(self):
        print("Execution time: %u sec %u usec" % (self.time.seconds, self.time.microseconds))

# Solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(0, len(nums) - 1):
            first = nums[i]

            for j in range(i + 1, len(nums)):
                second = nums[j]

                if first + second == target:
                    return [i, j]

# Test function
def test_solution(class_name):
    sol = class_name()

    time = Stopwatch()

    indices = sol.twoSum(nums, target)

    time.stop()

    # Print results
    #
    # Get int values by returned indices
    values = [nums[idx] for idx in indices]

    print("Result: Indices: %s Values: %s Sum: %u" %
        (str(indices), str(values), sum(values)))

    time.print()

    assert(sum(values) == target)

# Main
if __name__ == "__main__":
    print("Arguments: %s" % (str(sys.argv)))

    if len(sys.argv) == 1:
        print("%s: <target int> [int list]" % (sys.argv[0]))
        sys.exit(0)

    # Get target value
    target = int(sys.argv[1])

    # Convert the rest of argv to list of integers
    nums = []
    for i in range(2, len(sys.argv)):
        nums.append(int(sys.argv[i]))

    # Print input parameters
    print("Target: %i Integers: %s" % (target, str(nums)))

    # Test solution:
    test_solution(Solution)
