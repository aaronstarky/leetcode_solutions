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
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in range(len(nums)):
            if not counts.get(nums[i]):
                counts[nums[i]] = 0
            counts[nums[i]] += 1
        pq = []
        for key in counts:
            heapq.heappush(pq, (-1*counts[key], key))
        return [heapq.heappop(pq)[1] for i in range(k)]
    
solution = Solution()

print(solution.topKFrequent([1,1,1,2,2,3], 2))
print(solution.topKFrequent([1], 1))
