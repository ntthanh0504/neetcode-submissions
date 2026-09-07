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
        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < min(len(prefix), len(strs[i])):
                if prefix[j] != strs[i][j]:
                    break
                j += 1
            prefix = prefix[:j]
        return prefix