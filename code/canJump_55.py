class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:    # 当前下标可达最远位置。从数组的第一个位置开始，
                                  # 通过跳跃可以到达当前位置
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False

