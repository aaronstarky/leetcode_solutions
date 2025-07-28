# DONE

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        currSum, l, r = 0, 0, 0
        largestAv = float('-inf')
        while r < len(nums):
            currSum += nums[r]
            print(f"currSum = {currSum} = {currSum - nums[r]} + {nums[r]}");
            if r - l + 1 != k: 
                r += 1
                continue
            currAv = currSum / k
            if currAv > largestAv: largestAv = currAv
            r += 1
            l += 1
            currSum -= nums[l-1]
        return largestAv
    
solution = Solution()
print(f"Case 1: {solution.findMaxAverage([1,12,-5,-6,50,3], 4)}")
print(f"Case 2: {solution.findMaxAverage([5], 1) == 5}")
