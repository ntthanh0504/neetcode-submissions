class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in nums:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Expand the sequence forward as long as consecutive elements exist
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # Keep track of the maximum sequence length discovered so far
                longest_streak = max(longest_streak, current_streak)

        return longest_streak