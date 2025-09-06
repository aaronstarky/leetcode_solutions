# class Solution:
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
#     def trap(self, height: list[int]) -> int:
#         dp = [[0 for j in range(len(height))] for i in range(len(height))]
#         for i in range(len(height)):
#             largest = 0
#             for j in range(len(height)):
#                 if i == j:
#                     continue
#                 largest = max(height(j), largest)
#                 if not height(j) > largest:
#                     dp[i][j] = max(dp[i])
#                 prod = height[i] * height[j]
                
#     def trap(self, height: list[int]) -> int:
#         l = 0
#         for i in range(len(height)):
#             r = l + 1
#             while height[r] < height[]:
                
#     def get_peaks(self, height):
        
                
    
# print(Solution().trap([3,1,0,1,3]))

class Solution:
    def trap(self, height: list[int]) -> int:
        self.height = height
        pre_max = []
        post_max = []
        self.create_list(pre_max, range(len(height)), 0)
        self.create_list(post_max, range(len(height)-1, -1, -1), len(height)-1)
        post_max = post_max[::-1]
        # solve the problem
        total = 0
        for i in range(len(height)):
            calc = min(pre_max[i], post_max[i]) - height[i]
            added = 0 if calc < 0 else calc
            total += added
        return total

    def create_list(self, l, rang, cond):
        biggest = 0
        for i in rang:
            biggest = max(self.height[i], biggest)
            if i == cond:
                l.append(0)
                continue
            l.append(biggest)
