#!/usr/bin/python3

import sys

from typing import List

class Solution():

    def listStartsWith(self, strings:List[str], string:str) -> bool:
        if len(strings) == 0:
            return False

        for s in strings:
            if not s.startswith(string):
                return False

        return True

    def longestCommonPrefix(self, strings:List[str]) -> str:

        if len(strings) == 1:
            return strings[0]

        strings.sort(key=len)

        test_string = strings[0]

        for i in range(len(test_string), 0, -1):
            prefix = test_string[:i]

            if self.listStartsWith(strings[1:], prefix):
                return prefix

        return ""

if __name__ == "__main__":
    print("Args: %s" % (sys.argv))

    args = sys.argv[1:]

    solution = Solution()
    ret = solution.longestCommonPrefix(args)

    print("Args: %s" % (args))
    print("Ret:  %s" % (ret))
