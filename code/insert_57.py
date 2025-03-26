# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         result = []
#         for i in range(len(intervals)-1):
#             if i == 0 and newInterval[1]< intervals[i][0]:
#                 result.append(newInterval)
#             elif newInterval[0]>intervals[i][1] and newInterval[1] <intervals[i+1][0]:
#                 result.append(intervals[i])
#                 result.append(newInterval)
#             elif newInterval[0]<intervals[i][1]:
                

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # 1. 将所有在 `newInterval` 之前的区间添加到结果中
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # 2. 合并与 `newInterval` 重叠的区间
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)

        # 3. 将所有在 `newInterval` 之后的区间添加到结果中
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
    

    #与merge结合记