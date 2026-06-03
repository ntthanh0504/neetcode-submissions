class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            sum_x = numbers[left] + numbers[right]
            if sum_x == target:
                return [left + 1, right + 1]

            if sum_x < target:
                left += 1

            if sum_x > target:
                right -= 1

        return []