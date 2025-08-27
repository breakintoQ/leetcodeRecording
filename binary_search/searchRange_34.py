class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        result = []

        while l<r:
            mid = l+(r-l)//2
            if target<=nums[mid]:
                r = mid
            else:
                l = mid+1
        
        if not nums or nums[l]!= target :
            return [-1,-1]
        else:
            result.append(l)

        l=0
        r=len(nums)-1
#这个找到的是最后一个
        while l<r:
            mid = l+(r-l)//2
            if target<nums[mid]:
                r = mid
            else:
                l=mid+1

        if nums[l]==target:
            result.append(l)
        else:
            result.append(l-1)

        return result


#第二部分的循环可以这样：
# 寻找右边界的一个健壮写法
        # l = result[0] # 从左边界开始找就行，不用从0开始
        # r = len(nums) - 1
        
        # while l < r:
        #     # mid 向上取整，避免 l = mid 导致的死循环
        #     mid = l + (r - l + 1) // 2
        #     if target < nums[mid]:
        #         r = mid - 1
        #     else: # target >= nums[mid]   
        #根本：找右边界，等于时，答案可能在右侧，因此l右移，又因为mid可能是答案。所以等号放在放缩l的地方且l是mid
        
        # 此时 l 就是右边界
# 这题实在太经典了，我明天再看一遍