class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        i=0
        j=0
        while j < l:
            if nums[i]!= nums[j]:
                i+=1
                nums[i] = nums [j]
            j+=1
        return i+1