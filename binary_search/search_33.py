#还是先转换，保证能写出来，费空间，好像不是logn?
#不会写，官方思路是判断出一个有序区然后再分类
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:#前半区有序
                if nums[0] <= target < nums[mid]:#在前半区（因为前半区有序所以可以这样直接判断在前半区里）
                    r = mid - 1
                else:
                    l = mid + 1
            else:#后半区有序
                if nums[mid] < target <= nums[len(nums) - 1]:#在后半区（同理）
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

