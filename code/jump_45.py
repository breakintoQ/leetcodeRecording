# from typing import List

# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         l = len(nums)
#         k = 0
#         p = 0

#         while p < l - 1:
#             max_num = 0
#             max_index = -1
#             for i in range(p + 1, min(p + nums[p] + 1, l)):
#                 if max_num < i + nums[i]:
#                     max_num = i + nums[i]
#                     max_index = i
#             if max_index == -1:  # 如果没有找到更远的跳跃位置，说明无法继续跳跃
#                 break
#             p = max_index
#             k += 1
#         return k

#这个逻辑还是改不出来。下面是官方贪心，今天我实在太困了没看懂。
                

# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         n = len(nums)
#         maxPos, end, step = 0, 0, 0
#         for i in range(n - 1):
#             if maxPos >= i:
#                 maxPos = max(maxPos, i + nums[i])
#                 if i == end:
#                     end = maxPos
#                     step += 1
#         return step

