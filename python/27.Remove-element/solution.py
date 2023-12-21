class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        repl_idx = 0

        # Move non-val values to the head of array
        # then return new array size
        for n in nums:
            if n == val:
                continue

            nums[repl_idx] = n
            repl_idx += 1

        return repl_idx
