class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1

        if n ==1:
            return 0
        if n==2:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1
        
        while l<r:
            mid = l+(r-l)//2

            if nums[mid]<nums[mid+1]:
                l = mid+1
            elif nums[mid]>nums[mid+1]:
                r = mid

        return l

