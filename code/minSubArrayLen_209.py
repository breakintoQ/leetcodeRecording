# class Solution:
#     from typing import List
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         l = len(nums)
#         nums.sort()
#         windows = 1
#         while windows <=l:
#             if sum(nums[l-windows:l])>=target:
#                 return windows
#             else:
#                 windows+=1
#         return 0


#啊啊我服了是子数组不能sort


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        ans = n + 1   #最大化，初始化
        start, end = 0, 0   #窗口左右
        total = 0    #窗口内相加
        while end < n:
            total += nums[end]  
            while total >= s:   #缩小窗口，先缩小再前移
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1
        
        return 0 if ans == n + 1 else ans

# 


