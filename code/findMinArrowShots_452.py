# class Solution:
#     from typing import List
#     def findMinArrowShots(self, points: List[List[int]]) -> int:
#         l = len(points)
#         if l == 1:
#             return 1
#         points.sort(key = lambda x: x[0])
#         result = 0
#         i = 0
#         while i < l-1:
#             record = 0
#             for j in range (i+1,l):
#                 if points[j][0]<=points[i][1] and j < l-1:
#                     record +=1
#                     result +=1
#                 elif points[j][0]<=points[i][1] and j == l-1:
#                     record +=1
#                     result +=1
#                     i = j
#                 else:
#                     i = j
#                     break
#             if record == 0:
#                 result +=1
#         return result
    
# solution = Solution()

# points = [[10,16],[2,8],[1,6],[7,12]]

# result = solution.findMinArrowShots(points)

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # 按区间的结束位置排序
        points.sort(key=lambda x: x[1])
        
        arrows = 1  # 至少需要一支箭
        current_end = points[0][1]  # 第一个区间的结束位置
        
        for i in range(1, len(points)):
            # 如果当前区间的起始位置大于当前箭的覆盖范围
            if points[i][0] > current_end:
                arrows += 1  # 需要一支新的箭
                current_end = points[i][1]  # 更新箭的覆盖范围
        
        return arrows
    
    #贪心