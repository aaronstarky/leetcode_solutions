'''
This is my first attempt.

I think my error was trying to do everything in one loop
'''
# class Solution:
#     def topKFrequent(self, nums: list[int], k: int) -> list[int]:
#         podium = []
#         counts = {}
#         # O(n)
#         for i in range(len(nums)):
#             counts[nums[i]] = 1 + counts.get(nums[i], 0)
#             if len(podium) < k and nums[i] not in in_podium:
#                 podium.append(nums[i])
#                 in_podium.add(nums[i])
#             # O(k)
#             for j in range(len(podium)):
#                 # O(1)
#                 if counts[nums[i]] > counts[podium[j]]:
#                     podium.insert(nums[i])
#                     break
#         # O(n)
#         return podium[:k]    
    
    
'''
This is my second and successful solution. 

This was where my intuition initially took me, but I tried to get fancy and did the first attempt above.
'''
import heapq
    
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = {}
        # O(n)
        for i in range(len(nums)):
            counts[nums[i]] = 1 + counts.get(nums[i], 0)
        # O(n)
        heap = []
        for key in counts:
            heapq.heappush(heap, (counts[key] * -1, key))
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
    
solution = Solution()

print(solution.topKFrequent([1,1,1,2,2,3], 2))
print(solution.topKFrequent([1], 1))
