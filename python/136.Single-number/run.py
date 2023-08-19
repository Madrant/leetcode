#!/usr/bin/python3

import sys

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        countDict = {}

        for i in nums:
            if not i in countDict:
                countDict[i] = 1
            else:
                countDict[i] += 1

        for k in countDict:
            if countDict[k] == 1:
                return k

        return None

if __name__ == "__main__":
    print("Args: %s" % (sys.argv))

    nums = [int(i) for i in sys.argv[1:]]

    solution = Solution()
    ret = solution.singleNumber(nums)

    print("Ret: %s" % (ret))
