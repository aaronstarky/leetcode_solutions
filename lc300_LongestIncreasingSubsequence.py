class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        lengths = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and lengths[i] < lengths[j] + 1:
                    lengths[i] = lengths[j] + 1
        return max(lengths)
