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
        if not strs:
            return ""
            
        # Lấy từ đầu tiên làm chuẩn để so sánh
        first_word = strs[0]
        
        # Duyệt qua từng vị trí ký tự của từ đầu tiên
        for i in range(len(first_word)):
            char = first_word[i]
            
            # So sánh ký tự này với ký tự cùng vị trí ở các từ còn lại
            for other_word in strs[1:]:
                # Nếu chỉ số i vượt quá độ dài từ khác HOẶC ký tự không trùng khớp
                if i >= len(other_word) or other_word[i] != char:
                    return first_word[:i] # Cắt chuỗi từ đầu đến vị trí i
                    
        return first_word