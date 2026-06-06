class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # Bắt đầu với stack rỗng để code đồng nhất
        
        for i, t in enumerate(temperatures):
            # Chỉ cần kiểm tra: stack không rỗng VÀ nhiệt độ hiện tại lớn hơn nhiệt độ ở đỉnh stack
            while stack and t > temperatures[stack[-1]]:
                t_ind = stack.pop()
                res[t_ind] = i - t_ind
            
            stack.append(i)  # Luôn push index hiện tại vào stack
            
        return res

            
            

            