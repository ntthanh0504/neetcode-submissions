class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = Counter()
        for num in nums:
            hmap[num] += 1
        
        res = []
        for i in range(k):
            max_key = max(hmap, key=hmap.get)
            hmap[max_key] = -1
            res.append(max_key)
        return res