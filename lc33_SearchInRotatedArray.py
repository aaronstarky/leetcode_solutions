from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
            
        if len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1

        l, r = 0, len(nums) - 1
        while l <= r:
            if l == r:
                if nums[l] != target:
                    return -1
                return l
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            # rememeber that this condition is checking to see if the left half of the array is sorted, not which half we should move to yet
            if nums[l] <= nums[m]:
                if nums[l] <= target and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
    
solution = Solution()

print(solution.search([2,3,4,5,1], 1))