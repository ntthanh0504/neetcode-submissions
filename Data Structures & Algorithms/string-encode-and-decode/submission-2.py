class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            for ch in s:
                res += str(ord(ch)) + '#'
            res += ' '
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        prev_i = 0
        s_n = ''
        for i, ch in enumerate(s):
            if ch == '#':
                s_n += chr(int(s[prev_i:i]))
                prev_i = i + 1
            if ch == ' ':
                res.append(s_n)
                s_n = ''
        return res

                
