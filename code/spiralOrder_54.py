# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         rows = len(matrix)
#         columns = len(matrix[0])
#         pr = rows -1
#         pc = columns -1
#         i = 0
#         j = 0
#         result = []
#         flagr = 1
#         flagc = -1
#         while pr >= rows // 2 and pc >= columns // 2:
#             if i < pr and j < pc:
#                 result.append(matrix[i][j])
#                 i+= flagr
#             elif i < pr and j == pc :
#                 result.append(matrix[i][j])
#                 j+= flagc
#                 pc -= 1
#                 flagr = -flagr
#             elif i == pr and j < pc:
#                 result.append(matrix[i][j])
#                 i+= flagr
#                 pr -= 1
#                 flagc = -flagc
#         return result


from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        rows, columns = len(matrix), len(matrix[0])
        result = []
        #四个边界变量
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        
        while left <= right and top <= bottom:
            # 从左到右遍历上边界
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1
            
            # 从上到下遍历右边界
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                # 从右到左遍历下边界
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1
            
            if left <= right:
                # 从下到上遍历左边界
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
        
        return result


