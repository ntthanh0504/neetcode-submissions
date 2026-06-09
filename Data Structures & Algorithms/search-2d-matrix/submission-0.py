class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, (rows * cols) - 1

        while low <= high:
            mid = low + (high - low) // 2
            print(mid, mid//cols, mid % cols)
            if matrix[mid//cols][mid%cols] == target:
                return True
            
            if matrix[mid//cols][mid%cols] < target:
                low = mid + 1

            if matrix[mid//cols][mid%cols] > target:
                high = mid - 1

        return False