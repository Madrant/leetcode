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

# Straightforward solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(0, len(nums) - 1):
            first = nums[i]

            for j in range(i + 1, len(nums)):
                second = nums[j]

                if first + second == target:
                    return [i, j]

# List index based solution
class IndexSolution:
    def twoSum(seld, nums: List[int], target: int) -> List[int]:
        for i, val in enumerate(nums):
            second = target - val

            if second in nums and nums.index(second) != i:
                return [i, nums.index(second)]
        return []

# Dictionary based solution
class DictSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}

        for (first_idx, first) in enumerate(nums):
            second = target - first

            # Check if second value is in dictionary
            if second in d:
                # Return saved index of a second value
                # and current index
                return [d[second], first_idx]
            else:
                # Store index of a first value
                d[first] = first_idx

# Test function
def test_solution(class_name):
    sol = class_name()

    time = Stopwatch()

    indices = sol.twoSum(nums, target)

    time.stop()

    if indices is None:
        print("No result")
        return

    print("Result: Indices: %s" % (str(indices)))

    # Get int values by returned indices
    values = [nums[idx] for idx in indices]

    # Print results
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

    # Test solutions:
    test_solution(Solution)
    test_solution(IndexSolution)
    test_solution(DictSolution)
