# 121:  true
# -121: false
# 10:   false
class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Corner cases
        if x < 0:
            return False

        if x <= 9:
            return True

        # Check for palindromness
        s = str(x)

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True
