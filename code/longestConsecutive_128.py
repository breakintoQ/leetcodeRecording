class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums:
            return 0
        count = 1
        cnt = 1
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 0:
                continue
            elif nums[i+1]-nums[i] == 1:
                cnt+=1
            else:
                count = max(count,cnt)
                cnt = 1
        return max(count, cnt)