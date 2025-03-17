# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
#         l = len(citations)
#         h = 0
#         for i in range(l):
#             k = 0
#             for j in range(l):
#                 if citations[i]<=citations[j]:
#                     k+=1
#             if k >= citations[i]:
#                 h = max(h,citations[i])
#         return h

#有测试用例不通过

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i, c in enumerate(citations):
            if i < c:
                h = i + 1
            else:
                break
        return h
    
#降序排列, 停止的地方说明以后的引用次数都不会满足条件.