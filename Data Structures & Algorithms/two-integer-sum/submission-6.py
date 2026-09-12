class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = dict()
        for i, num in enumerate(nums):
            diff = target - num
            if num in hmap:
                return [hmap[num], i]
            hmap[diff] = i
        return []