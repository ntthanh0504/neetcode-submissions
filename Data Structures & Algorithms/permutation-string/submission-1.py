class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        target = Counter(s1)
        curr = Counter(s2[:k])

        if curr == target:
            return True

        for i in range(0, len(s2) - k):
            curr[s2[i]] -= 1
            curr[s2[i+k]] += 1

            if curr == target:
                return True

        return False