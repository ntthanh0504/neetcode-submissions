class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            corr_idx = nums[i] - 1
            if nums[i] > 0 and nums[i] < n and nums[i] != nums[corr_idx]:
                nums[i], nums[corr_idx] = nums[corr_idx], nums[i]
                continue
            i += 1

        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1
                
