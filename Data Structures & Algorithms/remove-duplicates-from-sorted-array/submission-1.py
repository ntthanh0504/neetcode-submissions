from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Con trỏ ghi: trỏ vào vị trí sẽ đặt phần tử không trùng lặp tiếp theo
        write = 1
        
        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1
                
        return write