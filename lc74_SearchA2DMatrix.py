from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])
        l, r = 0, (self.m * self.n) - 1
        if l == r:
            return True if matrix[0][0] == target else False
        while l <= r:
            if l == r - 1:
                if self.get_value(l) == target or self.get_value(r) == target:
                    return True
                break
            m = l + ((r - l) // 2)
            m_val = self.get_value(m)
            if m_val < target:
                l = m + 1
            elif m_val > target:
                r = m - 1
            else:
                return True
        return False

    def get_position(self, i):
        row = i // self.n
        col = i % self.n
        return (row, col)

    def get_value(self, i):
        pos = self.get_position(i)
        print(f'row {pos[0]} col {pos[1]}')
        return self.matrix[pos[0]][pos[1]]
