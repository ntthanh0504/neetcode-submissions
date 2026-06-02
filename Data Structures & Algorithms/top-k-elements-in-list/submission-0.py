class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < 2:
            return nums
        
        h_map = {}
        for num in nums:
            h_map[num] = h_map.get(num, 0) + 1
        
        return sorted(h_map, key=h_map.get, reverse=True)[:k]