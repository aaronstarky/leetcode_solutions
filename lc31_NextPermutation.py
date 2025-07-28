class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums

        if len(nums) == 2:
            tmp = nums[0]
            nums[0] = nums[1]
            nums[1] = tmp
            return nums
        # get rightmost element smaller than next element
        pivot = None
        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                pivot = i
        if pivot is None:
            return nums.sort()
        # find rightmost element greater than pivot
        swp = pivot + 1
        for i in range(pivot + 1, len(nums)):
            if nums[i] > nums[pivot]:
                swp = i
        # swap pivot and swp
        tmp = nums[pivot]
        nums[pivot] = nums[swp]
        nums[swp] = tmp
        l = pivot + 1
        r = len(nums) - 1
        while l < r:
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
            l += 1
            r -= 1
        return nums
    
soln = Solution()

print(soln.nextPermutation([1,2]))
print(soln.nextPermutation([1,3,2]))
print(soln.nextPermutation([2,3,1]))
print(soln.nextPermutation([5,4,7,5,3,2]))