import numpy as np

def print_triangle(costs, triangle):
    for i in range(len(triangle)):
            for j in range(len(triangle)):
                print(costs[i,j], end=' ')
            print('')

class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        """
        Loop
            The minimum cost of any position in the array is:
            Special cases:
            if start:
                costs[0][0] = triangle[0][0]
            if left edge, path is:
                costs[m][n] = costs[m-1][n] + triangle[m][n]
            elif right edge, path is:
                costs[m][n] = costs[m-1][n-1] + triangle[m][n]
            else:
                costs[m][n] = min(costs[m-1][n-1] + triangle[m][n], costs[m-1][n] + triangle[m][n])
        return min(costs[max_depth][:])
        """

        costs = np.zeros((4,4))
        print_triangle(costs, triangle)
        print(triangle[0][0])
        costs[0,0] = triangle[0][0]
        print_triangle(costs, triangle)
        if len(triangle) == 0:
            return costs[0,0]
        for m in range(1, len(triangle)):
            for n in range(m+1):
                if n == 0:
                    costs[m,n] = costs[m-1,n] + triangle[m][n]
                elif n == m:
                    costs[m,n] = costs[m-1,n-1] + triangle[m][n]
                else:
                    costs[m,n] = min(costs[m-1,n-1] + triangle[m][n], costs[m-1,n] + triangle[m][n])
        print('Triangle matrix')
        print_triangle(costs, triangle)
        rtrn_val = min(costs[len(triangle)-1][:])
        return rtrn_val


soln = Solution()
inp = [[2],[3,4],[6,5,7],[4,1,8,3]]
minimum = soln.minimumTotal(inp)
print(minimum)