# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         l = len(nums)
#         if l%2 == 0:
#             if target == nums[l//2]:
#                 return l/2
#             elif target == nums[l//2-1]:
#                 return l/2-1
#             elif target <nums [l//2] and target > nums[l//2-1]:
#                 return l/2
#             elif target >nums [l//2]:
#                 return self.searchInsert(nums[l//2:l],target)
#             else:
#                 return self.searchInsert(nums[0:l//2],target)
#         else:
#             if l ==1 :
#                 if target == nums[l//2]:
#                     return l//2
#                 else:
#             elif target > nums [l//2]:
#                 return self.searchInsert(nums[l//2:l],target)
#             elif target < nums [1//2]:
#                 return self.searchInsert(nums[0:l//2],target)

#写一半发现不对了，返回的下标不正常

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l
    
#不用递归。没那么复杂，想啥呢这是。记住最后循环结束条件是l=r+1，所以l的左边一定小于tar，r结尾，r的右边一定大于等于tar，l开头。
# 因此返回的l下标一定是所求位置。