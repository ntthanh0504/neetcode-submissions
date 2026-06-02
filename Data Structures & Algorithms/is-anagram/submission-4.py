class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        h_map = dict()
        # Solution 1:
        # for ch in s:
        #     if ch in h_map:
        #         h_map[ch] += 1
        #     else:
        #         h_map[ch] = 1
        
        # for ch in t:
        #     if ch in h_map:
        #         h_map[ch] -= 1
        #     else:
        #         return False
        
        # Solution 2
        for i in range(len(s)):
            h_map[s[i]] = h_map.get(s[i], 0) + 1
            h_map[t[i]] = h_map.get(t[i], 0) - 1

        return all(v == 0 for v in h_map.values())
        