from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        hmap = Counter()
        for ch in s:
            hmap[ch] += 1
        for ch in t:
            hmap[ch] -= 1
        for val in hmap.values():
            if val > 0:
                return False
        return True