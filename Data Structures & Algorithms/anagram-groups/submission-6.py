class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for ch in word:
                idx = ord(ch) - ord('a')
                count[idx] += 1
            hmap[tuple(count)].append(word)
        return list(hmap.values())