import queue

class Solution:
    def gardenNoAdj(self, n: int, paths: list[list[int]]) -> list[int]:
        # Breadth first search it seems like
        flowers = [1 for i in range(n)]
        adj_l = [[] for i in range(n)]
        # Populate Adj List
        for path in paths:
            adj_l[path[0]-1].append(path[1]-1)
        for i in range(n):
            taken = set()
            for adj in flowers[i]:
                taken.add(flowers[adj])
            while flowers[i] in taken:
                flowers[i] = (flowers[i] % 4) + 1
        return flowers

                

                

                
        
        return 0
    
soln = Solution()
n = 4
paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
print(soln.gardenNoAdj(n, paths))