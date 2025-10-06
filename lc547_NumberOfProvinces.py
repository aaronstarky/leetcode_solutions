"""
Lets do a hashset. If it is connected,
"""

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        checked = set()
        connected = {}
        # Loop through each
        for i in range(len(isConnected)):
            checked.add(i)
            if i not in connected:
                connected[i] = set()
                connected[i].add(i)
            for j in range(len(isConnected)):
                if i == j:
                    continue
                if isConnected[i][j] == 1:
                    checked.add(j)
                    connected[j] = connected[i]
        rtrn = set()
        for item in connected:
            rtrn.add(connected[item])
            
        return len(rtrn)
    
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
soln = Solution()
print(soln.findCircleNum(isConnected))