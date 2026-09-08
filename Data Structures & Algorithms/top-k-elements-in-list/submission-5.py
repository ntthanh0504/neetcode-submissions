class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = Counter()
        res = []

        for num in nums:
            hmap[num] += 1
        for i in range(0, k):
            max_key = max(hmap, key=hmap.get)
            res.append(max_key)
            hmap[max_key] = -1

        return res