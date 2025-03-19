# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         l = len(numbers)
#         # for i in range(l):
#         #     if numbers[i]>target:
#         #         l = i
#         #         break
#         for i in range(l):
#             for j in range(i+1,l):
#                 if numbers[i]+numbers[j] == target:
#                     return [i+1,j+1]
                
#双指针
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return []
    
    #好有意思，为什么这样最后可以找到呢，，
    