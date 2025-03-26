class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        #标记lambda用法
        result = []
        for interval in intervals:
            # 如果结果列表为空，或者当前区间与结果列表的最后一个区间不重叠
            if not result or interval[0] > result[-1][1]:
                result.append(interval)
            else:
                # 如果当前区间与结果列表的最后一个区间重叠，合并区间
                result[-1][1] = max(result[-1][1], interval[1])
        
        return result
    

# lambda 是一种简洁的方式，用于定义简单的匿名函数，常见的使用场景包括：

# 排序（sort 或 sorted）
# # 按列表中每个子列表的第一个元素排序
# intervals = [[3, 4], [1, 2], [5, 6]]
# intervals.sort(key=lambda x: x[0])
# print(intervals)  # 输出: [[1, 2], [3, 4], [5, 6]]

# 映射（map）
# nums = [1, 2, 3, 4]
# squared = list(map(lambda x: x ** 2, nums))
# print(squared)  # 输出: [1, 4, 9, 16]

# 筛选（filter）
# nums = [1, 2, 3, 4, 5]
# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print(even_nums)  # 输出: [2, 4]

# 累积（reduce）
# from functools import reduce
# nums = [1, 2, 3, 4]
# product = reduce(lambda x, y: x * y, nums)
# print(product)  # 输出: 24