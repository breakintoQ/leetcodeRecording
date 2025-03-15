# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         l = len(prices)
#         if list(reversed(sorted(prices))) == prices:
#             return 0
        
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)
        for i in range(1, n):
            ans += max(0, prices[i] - prices[i - 1])
        return ans
    
#贪心的逻辑最简单，无限次买入卖出，可以记为只要每天有利润就卖。
#股票最大利润四道题可以最后综合来看。