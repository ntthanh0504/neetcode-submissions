class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_all = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                prod_all *= num
            else:
                zero_count += 1

        res = []
        for i, num in enumerate(nums):
            if num != 0 and zero_count == 0:
                res.append(int(prod_all/num))
            elif num == 0 and zero_count == 1:
                res.append(prod_all)
            else:
                res.append(0)
        return res