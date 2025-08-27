class Solution:
    # def trap(self, height: list[int]) -> int:
    #     # keep l, r l = 0, r = l + 1
    #     # when height[r + 1] is less than height[r], count squares from l to r
    #     # [3, 1, 0, 1, 3]
    #     l, r = 0, 0
    #     total = 0
    #     while l < len(height):
    #         # find peak one
    #         while l + 1 < len(height) and height[r + 1] >= height[r]:
    #             l += 1
    #         print(f'l: {l}')
    #         # find peak two
    #         container_height = min(height[l], height[r])
    #         while l < r:
    #             total += container_height - height[l]
    #             l += 1
    #         print(f'l: {l}')
    #     return total
    
    def trap(self, height: list[int]) -> int:
        dp = [[0 for j in range(len(height))] for i in range(len(height))]
        for i in range(len(height)):
            largest = 0
            for j in range(len(height)):
                if i == j:
                    continue
                largest = max(height(j), largest)
                if not height(j) > largest:
                    dp[i][j] = max(dp[i])
                prod = height[i] * height[j]
                
    def trap(self, height: list[int]) -> int:
        l = 0
        for i in range(len(height)):
            r = l + 1
            while height[r] < height[]:
                
    def get_peaks(self, height):
        
                
    
print(Solution().trap([3,1,0,1,3]))