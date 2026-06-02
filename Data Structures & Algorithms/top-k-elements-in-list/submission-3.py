class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < 1:
            return nums
        
        f_map = {}
        for num in nums:
            f_map[num] = f_map.get(num, 0) + 1
        
        s_map = {}
        for key, v in f_map.items():
            if v in s_map:
                s_map[v].append(key)
            else:
                s_map[v] = [key]
        
        res = []
        n = len(nums)
        for i in range(n, 0, -1):
            if i in s_map:
                res.extend(s_map[i])

            if len(res) == k:
                break
        return res