class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == ".":
                    continue
                    
                # Calculate square index
                square_idx = (r // 3) * 3 + (c // 3)
                
                # Check for duplicates
                if val in rows[r] or val in cols[c] or val in squares[square_idx]:
                    return False
                    
                # Insert into respective sets
                rows[r].add(val)
                cols[c].add(val)
                squares[square_idx].add(val)
                
        return True
