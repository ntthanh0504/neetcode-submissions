class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        
        h_map = {}
        for s in strs:
            h_key = tuple(sorted(s))
            if h_key in h_map:
                h_map[h_key].append(s)
            else:
                h_map[h_key] = [s]
        
        return list(h_map.values())
