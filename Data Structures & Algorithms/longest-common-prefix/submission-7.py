# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if len(strs) == 1:
#             return strs[0]

#         hmap = Counter()
#         min_len = 300
#         for s in strs:
#             min_len = min(min_len, len(s))

#         res = ""
#         i = 0
#         while i < min_len:
#             for s in strs:
#                 hmap[s[i]] += 1

#             if hmap[s[i]] % len(strs) != 0:
#                 return res

#             res += s[i]
#             i += 1
#         return res

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]