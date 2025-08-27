class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = len(height)
        p1 = 0
        p2 = l-1
        max_storage = 0
        while p1<p2:
            max_storage = max(max_storage, min(height[p1],height[p2])*(p2-p1))
            if height[p1]<height[p2]:
                p1+=1
            else:
                p2-=1
        return max_storage
    

    #一次过了，疑似有点聪明了
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         l = len(height)
#         p1 = 0
#         p2 = l-1
#         max_storage = 0
#         while p1<p2:
#             max_storage = max(max_storage, min(height[p1],height[p2])*(p2-p1))
#             if height[p1]<height[p2]:
#                 p1+=1
#             else:
#                 p2-=1
#         return max_storage

#半年之后用的这种暴力枚举。没过，二重性能还是不行。
#原来的方法是一层循环从大到小找，确实比较好，之前咋想到的呢