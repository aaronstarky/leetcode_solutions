class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1 or len(nums) == 2:
            return max(nums)
        dp = [nums[i] for i in range(len(nums))]
        for i in range(1, len(nums)):
            if i < 2: 
                dp[i] = max(dp[i], dp[i-1])
                continue
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]

