class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = dict()
        for i, num in enumerate(nums):
            if num in h_map:
                return [h_map[num], i]
            h_map[target-num] = i