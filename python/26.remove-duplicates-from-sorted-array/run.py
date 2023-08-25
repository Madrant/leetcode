#!/usr/bin/python3

import sys

from typing import List

class Solution():

    def removeDuplicates(self, nums: List[int]) -> int:
        current = 0

        for next in range(1, len(nums)):

            if nums[current] != nums[next]:
                current += 1
                nums[current] = nums[next]

        return current + 1

if __name__ == "__main__":
    print("Args: %s" % (sys.argv))

    args = sys.argv[1:]

    solution = Solution()
    ret = solution.removeDuplicates(args)

    print("Args: %s" % (args))
    print("Ret:  %s" % (ret))
