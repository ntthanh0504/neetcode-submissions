class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            sum_x = numbers[l] + numbers[r]
            if sum_x == target:
                return [l + 1, r + 1]
            elif sum_x < target:
                l += 1
            else:
                r -= 1
            