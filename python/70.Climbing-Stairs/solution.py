class Solution:

    def __init__(self):

        # dict to cache recursive cases
        self.d = {}

        # Recursion base cases:
        self.d[1] = 1
        self.d[2] = 2

    def climbRecurse(self, n: int) -> int:

        if n in self.d:
            return self.d[n]
        else:
            self.d[n] = self.climbRecurse(n - 1) + self.climbRecurse(n - 2)
            return self.d[n]

    def climbStairs(self, n: int) -> int:

        # Call recursive function as next = way(n - 1) + way(n - 2)
        #
        # Example:
        # 3 = way(2) + way(1)
        return self.climbRecurse(n)
