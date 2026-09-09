class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hmap = Counter()
        for num in nums:
            hmap[num] += 1

        res = []
        for k, v in hmap.items():
            if v > n/3:
               res.append(k)
        return res 
