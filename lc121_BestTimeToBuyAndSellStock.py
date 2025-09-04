# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         if len(prices) == 1:
#             return 0
#         best = 0
#         for i in range(len(prices)-1):
#             for j in range(i + 1, len(prices)):
#                 profit = prices[j] - prices[i]
#                 if profit > best:
#                     best = profit
#         return best

'''
This solution below me that I pulled from leetcode is so good.
Super simple. It updates the best possible price for buying as
it goes. Stores profit between iterations and subtracts the buy
price from the current nubmer to compare max.
'''
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        price = prices[0]
        profit = 0
        
        for p in prices[1:]:
            if price > p:
                price = p
            profit = max(profit, p - price)
        return profit
