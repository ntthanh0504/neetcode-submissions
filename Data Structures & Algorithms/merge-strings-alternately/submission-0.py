class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        i = j = 0
        res = ""
        while i < n and j < m:
            res += (word1[i] + word2[j])
            i, j = i + 1, j + 1

        if i < n:
            res += word1[i:]
        if j < m:
            res += word2[j:]
        return res 
