class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        n = len(nums)
        
        for i in range(n):
            # Bỏ qua phần tử trùng lặp cho vị trí thứ nhất
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            target = -nums[i]
            # Con trỏ left luôn bắt đầu SAU vị trí i
            left, right = i + 1, n - 1
            
            while left < right:
                sum2 = nums[left] + nums[right]
                
                if sum2 == target:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif sum2 < target:
                    left += 1
                else:
                    right -= 1
                    
        return res
