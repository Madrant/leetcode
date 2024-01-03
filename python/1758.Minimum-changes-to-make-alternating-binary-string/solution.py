class Solution:
    def minOperations(self, s: str) -> int:

        # Get next alterating value
        n = '1' if int(s[0]) == 0 else '0'

        # Count operations
        ops = 0

        # For each char except first
        for c in s[1:]:

            # If char is not as expected
            if c != n:
                ops += 1

            # Get next alterating value
            n = '0' if n == '1' else '1'

        # Return minimum required operations
        return min(ops, len(s) - ops)
