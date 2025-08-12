class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        # sort the array
        nums.sort()
        # create needed values
        dp = [1 for i in range(len(nums))]
        curr = 1
        for i in range(1, len(nums)):
            if nums[i]-1 == nums[i-1]:
                curr += 1
            elif nums[i]-1 > nums[i-1]:
                curr = 1
            dp[i] = max(curr, dp[i-1])
        return dp[-1]

        