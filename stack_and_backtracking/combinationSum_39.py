# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         path = []
#         result = []

#         def backtrack():
#             if sum(path[:]) == target:
#                 result.append(path[:])
#                 return
            
#             for i in range(len(candidates)):
#                 path.append(candidates[i])
#                 backtrack()
#                 path.pop()
            
        
#         backtrack()
#         return result


from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        result = []
        
        # 💡 优化点：先排序，有助于提前剪枝
        candidates.sort()

        # 增加了 current_sum 和 start_index 参数
        def backtrack(current_sum, start_index):
            # 剪枝：如果当前和已经超过目标，直接返回
            if current_sum > target:
                return
            
            # 终止条件：如果当前和等于目标，找到一个解
            if current_sum == target:
                result.append(path[:])
                return
            
            # 从 start_index 开始遍历，避免重复组合
            for i in range(start_index, len(candidates)):
                num = candidates[i]
                
                # 💡 又一个剪枝：如果当前和加上 num 都大于 target，
                # 并且因为数组已排序，后面的数更大，所以没必要再试了
                if current_sum + num > target:
                    break
                
                # 做出选择
                path.append(num)
                # 递归：因为元素可以重复使用，下一次递归还是从 i 开始
                backtrack(current_sum + num, i)
                # 撤销选择
                path.pop()
        
        # 初始调用
        backtrack(0, 0)
        return result
    
#记住剪枝条件