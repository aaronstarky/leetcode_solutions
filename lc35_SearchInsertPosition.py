class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if l == r:
                if nums[l] >= target:
                    return l
                else:
                    return l + 1
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m
            else:
                l = m + 1
        


solution = Solution()

print(solution.searchInsert([1,3,5,6], 2))
print(solution.searchInsert([1,3,5,6], 7))

