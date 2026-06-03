class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_v = 0
        
        while left < right:
            # Calculate current volume using the shorter wall
            current_v = min(heights[left], heights[right]) * (right - left)
            
            # Update running maximum in-place
            if current_v > max_v:
                max_v = current_v
                
            # Move the pointer pointing to the shorter wall inward
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_v