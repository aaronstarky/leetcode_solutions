class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # sort for guarantees
        nums.sort()
        best = float('inf')
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == target:
                    return target
                elif total < target:
                    j += 1
                else:
                    k -= 1
                
                if self.distance(target, total) < self.distance(target, best):
                    best = total
                while nums[j] == nums[j-1] and j < k:
                    j += 1
                
        return best

    def distance(self, num1, num2):
        return num2 - num1
        # if num1 < num2:
        #     return abs(num2 - num1)
        # else:
        #     return abs(num1 - num2)
        
        
        
soln = Solution()

case1 = [0,0,0]
print(soln.threeSumClosest(case1, 1))
case2 = [-1000,-5,-5,-5,-5,-5,-5,-1,-1,-1]
print(soln.threeSumClosest(case2, -14))