class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = Counter()
        for num in nums:
            hmap[num] += 1
        return max(hmap, key=hmap.get)
        