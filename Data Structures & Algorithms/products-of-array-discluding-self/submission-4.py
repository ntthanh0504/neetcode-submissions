class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # Step 1: Calculate Prefix products (All elements to the left of i)
        # res[i] will store the product of all numbers from nums[0] up to nums[i-1]
        prefix_product = 1
        for i in range(n):
            res[i] = prefix_product
            prefix_product *= nums[i]

        # Step 2: Calculate Suffix products on the fly and multiply with Prefix products
        # We iterate backwards from the end of the array down to the beginning
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            # Combined product = (Existing Prefix in res[i]) * (Current Suffix)
            res[i] *= suffix_product
            suffix_product *= nums[i]

        return res