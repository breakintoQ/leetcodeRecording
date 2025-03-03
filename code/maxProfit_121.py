# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         length=len(prices)
#         max_profit = 0
#         for i in range(0,length,1):
#             for j in range(i,length,1):
#                 temp=prices[j]-prices[i]
#                 if  max_profit<temp:
#                     max_profit=temp
#         return max_profit
                    

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost, profit = float('+inf'), 0
        for price in prices:
            cost = min(cost, price) #一开始cost最大
            profit = max(profit, price - cost)
        return profit


"""
一拿到觉得很简单没啥思维难度后来果然超时了嗯啊。新解法的目的就是两个贪心。首先当前最小cost，然后依据该cost更新最小利润
跟数组完全没关系啊不知道为什么放进这个组里了，不能因为数据结构是数组就这样吧。
思想是一点没有的，算法书都卖了（，学过的东西也都就饭吃了，还得加强思想啊kora
"""