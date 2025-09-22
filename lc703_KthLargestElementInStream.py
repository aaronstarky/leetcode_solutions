import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        print(len(nums))
        self.heap = []
        self.k = k
        nums.sort()
        nums = nums[::-1]
        for i in range(min(k, len(nums))):
            heapq.heappush(self.heap, nums[i])

    def add(self, val: int) -> int:
        # insert val into it's proper place in self.k_largest
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        
