class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        stack.append(0)
        for i in range(1, len(temperatures)):
            t_ind = stack[-1]
            while temperatures[i] > temperatures[t_ind]:
                res[t_ind] = i-t_ind
                stack.pop()
                if len(stack) == 0:
                    break
                
                t_ind = stack[-1]
            
            stack.append(i)

            print(i, stack, res)

        return res

            
            

            