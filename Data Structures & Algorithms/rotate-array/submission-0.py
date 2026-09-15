class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        res = [0] * n

        for i in range(n):
            n_idx = (i + k) % n
            res[n_idx] = nums[i]
        
        nums[:] = res