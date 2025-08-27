class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l = len(nums)
        i = 0
        j = 0

        while j<l:
            if nums[i] ==0:
                if nums[j]!=0:
                    nums [i],nums[j]= nums[j],nums[i]
                    i+=1
            else:
                i+=1
            j+=1