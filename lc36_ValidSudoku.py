from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        grids = defaultdict(set)
        for r in range(9):
            row = set()
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                if board[r][c] in row or board[r][c] in cols[c] or board[r][c] in grids[self.map_indices_to_grid(r, c)]:
                    return False
                row.add(board[r][c])
                cols[c].add(board[r][c])
                grids[self.map_indices_to_grid(r, c)].add(board[r][c])
        return True
        
    def map_indices_to_grid(self, row, col):
        return ((row // 3) * 3) + (col // 3)
    
    
    

solution = Solution()

input1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
input2 = [["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

print(solution.isValidSudoku(input1))
print(solution.isValidSudoku(input2))