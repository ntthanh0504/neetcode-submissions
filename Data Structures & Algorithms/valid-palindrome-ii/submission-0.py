class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                # Trường hợp 1: bỏ s[l] -> kiểm tra s[l+1 : r+1]
                skip_l = s[l + 1 : r + 1]
                # Trường hợp 2: bỏ s[r] -> kiểm tra s[l : r]
                skip_r = s[l : r]
                
                return skip_l == skip_l[::-1] or skip_r == skip_r[::-1]
            
            l += 1
            r -= 1
            
        return True