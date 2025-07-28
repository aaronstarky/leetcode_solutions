class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        result = self.countAndSay(n-1)
        count = 0
        val = result[0]
        rtrn = ''
        for i in range(len(result)):
            if result[i] == val:
                count += 1
            else:
                rtrn += str(count) + val
                val = result[i]
                count = 1
        rtrn += str(count) + val
        return rtrn
        
        
solution = Solution()
print(solution.countAndSay(1))
print(solution.countAndSay(4))
