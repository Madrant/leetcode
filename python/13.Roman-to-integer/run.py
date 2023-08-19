#!/usr/bin/python3

import sys

class Solution:
    def romanToInt(self, s: str) -> int:

        rDict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        r2Dict = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        ret = 0
        i = 0

        while i < len(s):
            l2 = s[i:i + 2]
            l1 = l2[0]

            if l2 in r2Dict:
                ret += r2Dict[l2]
                i += 2
            else:
                ret += rDict[l1]
                i += 1

        return ret

if __name__ == "__main__":
    print("Args: %s" % (sys.argv))

    roman = sys.argv[1]

    solution = Solution()
    ret = solution.romanToInt(roman)

    print("Ret: %i" % (ret))
