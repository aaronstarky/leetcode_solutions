class Solution:
    def maxArea(self, heights: list[int]) -> int:
        largest = 0
        l, r = 0, len(heights) - 1
        while l < r:
            height = min(heights[l], heights[r])
            length = r - l
            product = height * length
            largest = max(largest, product)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return largest