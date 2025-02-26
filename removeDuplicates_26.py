class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        p = 0
        for i in range (0,length,1):
           if nums[i]!=nums[p]:
               p+=1
               nums[p]=nums[i]
        return p+1


"""
自己写时间复杂度贼高但是还不通过，题解就两行，复杂度也小。双指针很容易想但是折腾不清了。
这个是看的别人的解，思路是重复就跳过，直到不一样的时候将目前快指针的值赋给慢指针+1，也就是重复的那个值。这里的思路重点
发现我是没仔细看题啊，非严格递增说明重复的肯定挨着，直接替换下一个就好了，不存在覆盖的问题。
相当于快指针只要找到不一样的就拿到前边去了，不可能覆盖因为快的已经跑过一遍了。
嗯嗯。
"""