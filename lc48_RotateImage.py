class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        nums = []
        n = len(matrix)
        for j in range(n):
            for i in range(n-1, -1, -1):
                nums.append(matrix[i][j])
        for i in range(n):
            for j in range(n):
                matrix[i][j] = nums[i*n + j]
