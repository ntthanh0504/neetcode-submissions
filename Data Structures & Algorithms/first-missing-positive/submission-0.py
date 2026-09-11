class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            t_idx = nums[i] - 1
            if nums[i] > 0 and nums[i] <= n and nums[i] != nums[t_idx]:
                nums[i], nums[t_idx] = nums[t_idx], nums[i]
                continue
            i += 1
        
        for i in range(0, n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
            
