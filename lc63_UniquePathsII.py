class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        paths: list[list[int]] = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        paths[0][0] = 1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1: 
                    paths[i][j] = 0
                else:
                    up, left= 0, 0
                    if i != 0:
                        up = paths[i-1][j]
                    if j != 0:
                        left = paths[i][j-1]
                    paths[i][j] += up + left 
                
        return paths[-1][-1]
        
print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
print(Solution().uniquePathsWithObstacles([[0,1],[0,0]]))
print(Solution().uniquePathsWithObstacles([[1,0]]))
print(Solution().uniquePathsWithObstacles([[0,1,0,0]]))
print(Solution().uniquePathsWithObstacles([[0]]))
