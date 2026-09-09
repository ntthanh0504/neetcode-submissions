class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = Counter()
        prefix = 0
        res = 0

        prefix_map[prefix] = 1

        for i, num in enumerate(nums):
            prefix += num
            diff = prefix - k

            if diff in prefix_map:
                res += prefix_map[diff]
            
            prefix_map[prefix] += 1

        return res