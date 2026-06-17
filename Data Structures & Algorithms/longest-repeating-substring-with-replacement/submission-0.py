class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        longest = 0
        window_counter = Counter()
        for end in range(0, len(s)):
            lead_ch = s[end]
            window_counter[lead_ch] += 1
            most_freq = max(window_counter.values())
            while (end-start + 1) - most_freq > k:
                trail_ch = s[start]
                window_counter[trail_ch] -= 1
                start += 1
            longest = max(end-start+1, longest)
        return longest
