#!/usr/bin/python3

import sys

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        base = 10

        if len(digits) == 0:
            return [0]

        if len(digits) == 1 and digits[0] == base - 1:
            return [1, 0]

        if digits[-1] == base - 1:
            return self.plusOne(digits[:len(digits) - 1]) + [0]
        else:
            digits[-1] += 1
            return digits

if __name__ == "__main__":
    print("Args: %s" % (sys.argv[1:]))

    digits = [int(i) for i in sys.argv[1:]]

    solution = Solution()
    retList = solution.plusOne(digits)

    print("Result: %s" % (retList))
