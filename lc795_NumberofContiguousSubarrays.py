class Solution:    
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        return self.count(nums, right) - self.count(nums, left-1)

    def count(self, l, bound):
        c = 0
        answer = 0
        
        for i in range(len(l)):
            if l[i] <= bound:
                c += 1
            else:
                answer += c*(c + 1)//2
                c = 0
        return answer + c*(c + 1)//2

print(Solution().numSubarrayBoundedMax([2,1,4,3], 2, 3))
print(Solution().numSubarrayBoundedMax([2,9,2,5,6], 2, 8))


