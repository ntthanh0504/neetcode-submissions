class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i, ch in enumerate(strs[0]):
            for s in strs[1:]:
                if i > len(s) - 1 or ch != s[i]:
                    return res
            res += ch
        return res