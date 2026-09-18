class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        curr_num = 0

        for ch in s:
            if ch.isdigit():
                # Xử lý số có nhiều chữ số liên tiếp (vd: 12 -> 1 * 10 + 2)
                curr_num = curr_num * 10 + int(ch)
            elif ch == '[':
                # Lưu lại chuỗi trước đó và số lần lặp cho khối ngoặc hiện tại
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0
            elif ch == ']':
                prev_str, num = stack.pop()
                # Nhân chuỗi trực tiếp và ghép vào chuỗi cấp trước
                curr_str = prev_str + curr_str * num
            else:
                curr_str += ch

        return curr_str