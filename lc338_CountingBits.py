class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0 for _ in range(n + 1)]
        offset = 1
        for i in range(1,n+1):
            if 2 * offset == i:
                offset = i
            dp[i] = dp[i - offset] + 1
        return dp
