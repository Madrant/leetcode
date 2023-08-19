#!/usr/bin/python3

import sys
import time

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsDict = {}

        for i in nums:
            if not i in numsDict:
                numsDict[i] = 1
            else:
                numsDict[i] += 1

        if numsDict[i] >= 2:
            return True

        return False

if __name__ == "__main__":
    print("Arguments: {0}".format(str(sys.argv)))

    args = sys.argv[1:]

    start = time.time()

    solution = Solution()
    ret = solution.containsDuplicate(args)

    end = time.time()

    print(f"args: {args}")
    print(f"ret:  {ret}")
    print("time: %f sec" % (end - start))
