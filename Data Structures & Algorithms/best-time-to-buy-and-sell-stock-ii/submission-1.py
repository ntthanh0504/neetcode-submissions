# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0
#         for i in range(0, len(prices) - 1):
#             diff = prices[i+1] - prices[i]
#             if diff > 0:
#                 max_profit += diff
#         return max_profit

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        
        # Khởi tạo trạng thái ngày 0:
        # hold: Mua ngay ngày 0 -> lợi nhuận là -prices[0]
        # empty: Chưa làm gì -> lợi nhuận là 0
        hold = -prices[0]
        empty = 0
        
        for price in prices[1:]:
            # Lưu lại trạng thái cũ để tránh bị ghi đè khi cập nhật
            prev_hold = hold
            prev_empty = empty
            
            hold = max(prev_hold, prev_empty - price)
            empty = max(prev_empty, prev_hold + price)
            
        return empty