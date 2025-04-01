# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         l = len(nums)
#         p1 = 0
#         p2 = 1
#         flag = 0
#         k = 0
#         while p1<l and p2 <l:
#             if nums[p1] == nums[p2]:
#                 while nums[p2] == nums[p1] and p2<l:
#                     flag+=1
#                     p2+=1
#                 if flag>=2:
#                     for flag in range(flag,1,-1):
#                         nums[p2-flag+1] = nums[p2]
#                         k+=1
#                 p1+=2
#                 p2 = p1+1
#             else:
#                 p1 += 1
#                 p2 = p1+1
#         return l-k
    

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        slow, fast = 2, 2
        while fast < n:
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

#思路还是不太对。
# 使用两个指针 slow 和 fast，初始值都为2。slow 指针用于构建新的数组，fast 指针用于遍历原数组。
# slow 指针指向新数组的下一个可插入位置，fast 指针用于遍历原数组。
# 使用 while 循环遍历数组，直到 fast 指针到达数组末尾。
# 在每次循环中，检查 nums[slow - 2] 和 nums[fast] 是否相等。
# 如果不相等，说明当前元素可以插入到新数组中，将 nums[fast] 赋值给 nums[slow]，并将 slow 指针向前移动一位。
# 如果相等，说明当前元素已经在新数组中出现了两次，不需要再插入，直接将 fast 指针向前移动一位。
# 其实跟只能出现一个重复的思路一样，一个慢指针用来构建快指针用来遍历，只要不在代构建数组中（在数组中次数小于2）
# 的进行赋值。