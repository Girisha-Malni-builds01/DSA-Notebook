class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)

        # Mark visited numbers
        for i in range(n):
            idx = abs(nums[i]) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        # Numbers which remain positive were never visited
        result = []
        for i in range(n):
            if nums[i] > 0:
                result.append(i + 1)

        return result
