#!/usr/bin/python3

import sys

class Solution:

    def isValid(self, s: str) -> bool:
        # Odd number of brackets
        if len(s) % 2 != 0:
            return False

        left = list("({[")
        right = list(")}]")

        # String starts from close bracket
        if s[0] in right:
            return False

        # Check perentheses num
        bracket_types = [1 if i in left else 0 for i in s]

        if bracket_types.count(1) != bracket_types.count(0):
            return False

        # Open brackets must be closed in the correct order
        nextDict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        next_stack = []

        for c in s:
            if c in left:
                next_stack.append(nextDict[c])
                continue

            # Closed bracket in wrong place
            if len(next_stack) == 0:
                return False

            if c != next_stack[-1]:
                return False
            else:
                next_stack.pop()

        # All checks has passed
        return True

if __name__ == "__main__":
    print("Args: %s" % (sys.argv))

    arg = sys.argv[1]

    solution = Solution()
    ret = solution.isValid(arg)

    print(f"Arg: {arg}")
    print(f"Ret: {ret}")
