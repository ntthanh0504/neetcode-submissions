# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
        
#         h_map = dict()
#         for ch in s:
#             if ch in h_map:
#                 h_map[ch] += 1
#             else:
#                 h_map[ch] = 1
        
#         for ch in t:
#             if ch in h_map:
#                 h_map[ch] -= 1
#             else:
#                 return False
        
#         for v in h_map.values():
#             if v != 0:
#                 return False

#         return True
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True