class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        shortest = len(s)
        res = ""
        target = Counter(t)
        window = Counter()
        need = len(target)
        have = 0
        for end in range(0, len(s)):
            lead_ch = s[end]
            window[lead_ch] += 1
            if s[end] in target and window[lead_ch] == target[lead_ch]:
                have += 1

            while have == need:
                if end - start + 1 <= shortest:
                    shortest = end - start + 1
                    res = s[start:end+1]
                    print("shortest", shortest, "res", res)

                trail_ch = s[start]
                window[trail_ch] -= 1
                if s[start] in target and window[trail_ch] < target[trail_ch]:
                    have -= 1

                print("in: ", have)
                print("start: ", start, "end: ", end, "s[start]", s[start])

                

                start += 1

        return res
