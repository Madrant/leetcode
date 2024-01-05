class Solution:
    def mySqrt(self, x: int) -> int:

        # Use binary search on [0...x]
        low = 0
        high = x

        while low <= high:

            mid = (low + high) // 2

            pow = mid * mid

            if pow == x:
                return mid

            if pow > x:
                high = mid - 1
            else:
                low = mid + 1

        return high
