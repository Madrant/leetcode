class Solution:

    # nums contains distinct values sorted in ascending order
    def searchInsert(self, nums: List[int], target: int) -> int:

        # Use binary search
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            val = nums[mid]

            if val == target:
                return mid

            if val > target:
                high = mid - 1
            else:
                low = mid + 1

        # target not found - return expected position
        return high + 1
