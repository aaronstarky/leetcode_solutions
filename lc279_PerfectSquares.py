import numpy as np

class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        low_bound = np.floor(np.sqrt(n))
        for i in range(1,n):
            if i > low_bound:
                break
            squares.append(i**2)  
        start = len(squares)-1
        i = start 
        rem = n 
        count = 0
        counts = []
        while i >= 0:
            
            if rem < 0:
                start -= 1
                i = start
                rem = n
                count = 0
                continue
            if squares[i] > rem: 
                i -= 1
                continue
            mod = n % squares[i]
            if mod == 0 and count == 0:
                count += n / squares[i]
                counts.append(count)
                rem = -1 
                continue
            mod = rem % squares[i]
            if mod == 0:
                count += rem / squares[i]
                counts.append(count)
                rem = -1
                continue
            else:
                count += rem // squares[i]
                rem -= squares[i] * (rem // squares[i])
                i -= 1
        return min(counts)
                

soln = Solution()
n = 43

print(soln.numSquares(n))
        

        
            

        