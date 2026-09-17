class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, tmp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < tmp:
                idx = stack.pop()
                res[idx] = i - idx
            else:
                stack.append(i)

        return res

        # 30 : 0
        # 38 : pop 0 -> push 1 -> [1] -> res[0] = 1
        # 30 : push [2] -> [1, 2]
        # 36 : pop 2 -> push 3 -> [1, 3] -> res[2] = 3 - 2
        # 35 : push 4 -> [1, 3, 4] 
        # 40 : pop 4 -> pop 3 -> pop 1 -> push 5 -> [5] res[4] = 5 - 4, 
        # 28 : push 6 [5, 6]
            
            

            