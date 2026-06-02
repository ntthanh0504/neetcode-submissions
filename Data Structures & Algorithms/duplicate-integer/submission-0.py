class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnts = {}
        for num in nums:
            if num in cnts:
                cnts[num] += 1
            else:
                cnts[num] = 1
                
            if cnts[num] > 1:
                return True
        return False