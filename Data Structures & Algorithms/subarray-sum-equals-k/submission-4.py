class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = Counter()
        sum_x = 0
        hmap[sum_x] += 1
        res = 0
        for num in nums:
            sum_x += num
            diff = sum_x - k
            if diff in hmap:
                res += hmap[diff]
            hmap[sum_x] += 1
        return res