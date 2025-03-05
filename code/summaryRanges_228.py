class Solution:
    from typing import List
    def summaryRanges(self, nums: List[int]) -> List[str]:
        list1 = []
        l = len(nums)
        p1 = 0
        p2 = 1
        temp = nums[0]
        while  p1<l-1 and p2 <l :
            if nums[p2]-nums[p1]>1:
                if p1 == 0:
                    list1.append(str(nums[p1]))
                    temp = nums[p2]
                elif p2 == l-1:
                    if temp != nums[p2-1]:
                        list1.append(str(temp)+"->"+str(nums[p2-1]))
                    list1.append((str(nums[p2])))
                elif nums[p2+1]-nums[p2]>1 and p2<l-1:
                    list1.append(str(nums[p1]))
                    temp = nums[p2]
                else:
                    list1.append(str(temp)+"->"+str(nums[p1]))
                    temp = nums[p2]
            p1+=1
            p2+=1
        return list1



# class Solution:
#     def summaryRanges(self, nums: List[int]) -> List[str]:
#         result = []
#         i = 0
#         n = len(nums)
#         while i < n:
#             low = i
#             i += 1
#             while(i < n and nums[i] == nums[i - 1] + 1):
#                 i += 1     这里多加了一边因此要减掉，下一遍从加完的i为起始点开始遍历。也就是实际上区间为0，1，但是i已经加到2，下一遍已2为起始
#             high = i - 1   
#             if (low < high):
#                 result.append(str(nums[low]) + "->" + str(nums[high]))
#             else:
#                 result.append(str(nums[low]))
#         return result

# 自己写没写出来，注释的是给出的题解。思路很简单但是实现出问题了，判断条件有问题，两重循环找high确实是很好，