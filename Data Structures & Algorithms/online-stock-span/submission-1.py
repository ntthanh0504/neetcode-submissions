class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1] <= price:
            self.stack.pop() # pop prev price
            prev_span = self.stack.pop()
            span += prev_span
        else:
            self.stack.append(span)
            self.stack.append(price)
        return span


# # Your StockSpanner object will be instantiated and called as such:
# # obj = StockSpanner()
# # param_1 = obj.next(price)
# price    action      stack
# 100   -> push 100 -> 1, 100
# 80    -> pop 100  -> 1, 100, 1, 80
#          push 80 
# 60                -> 1, 100, 1, 80, 1, 60
# 70    -> pop 60 push 70 -> 1, 100, 1, 80, 2, 70
# 60    -> push 60 -> 100, 80, 70, 1, 60
# 75    -> pop 60, pop 70, push 75 -> 100, 80, 75
