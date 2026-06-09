class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        min_k = high

        while low <= high:
            k = low + (high - low) // 2
            cal_h = 0
            
            # Tính tổng số giờ cần thiết với vận tốc k
            for pile in piles:
                # math.ceil dùng để làm tròn lên (VD: 3 quả, vận tốc 2 -> mất 2 giờ)
                cal_h += math.ceil(pile / k)
            
            # Nếu ăn kịp trong h giờ, cố gắng tìm vận tốc nhỏ hơn nữa
            if cal_h <= h:
                min_k = k
                high = k - 1
            # Nếu không ăn kịp, buộc phải tăng vận tốc lên
            else:
                low = k + 1

        return min_k

