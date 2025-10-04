class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            if l == r or l == r - 1:
                return min(nums[l], nums[r])
            m = l + ((r-l)//2)
            if nums[l] > nums[m]:
                r = m
            elif nums[m] > nums[r]:
                l = m
            else:
                r = m
