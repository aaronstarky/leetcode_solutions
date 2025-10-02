class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}
        dp[(0,0)] = 1
        for i in range(m):
            for j in range(n):
                if i == j == 0: continue
                up = dp.get((i-1,j), 0)
                left = dp.get((i,j-1),0)
                dp[(i,j)] = up + left
        return dp[(m-1,n-1)]
