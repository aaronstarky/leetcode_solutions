class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        lengths = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and lengths[i] < lengths[j] + 1:
                    lengths[i] = lengths[j] + 1
        return max(lengths)

class BinarySearchSolution(object):
    def lengthOfLIS(self, nums):
        seq = []
        for i in range(len(nums)):
            if len(seq) == 0 or seq[-1] > nums[i]:
                seq.append(nums[i])
            else:
                index = bisect_left
                
    def bisect_left(self, seq, target):
        l, r = 0, len(seq) - 1
        while l < r:
            m = l + ((r - l) // 2)
            if seq[m] < target:
                l = m + 1
            