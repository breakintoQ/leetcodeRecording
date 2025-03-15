class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        if k>l:
            k=k%l
        cache = []
        cache[:k] = nums[l-k:]
        cache[k:] = nums[0:l-k]
        nums[:] = cache[:]




#空间复杂度不是o1，我看看别的解法。

# 该方法基于如下的事实：当我们将数组的元素向右移动 k 次后，尾部 kmodn 个元素会移动至数组头部，
# 其余元素向后移动 k mod n 个位置。

# 该方法为数组的翻转：我们可以先将所有元素翻转，这样尾部的 k mod n 个元素就被移至数组头部，
# 然后我们再翻转 [0,k mod n−1] 区间的元素和 [k mod n,n−1] 区间的元素即能得到最后的答案。
#我就说记得还有一个反转。写写试试

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l = len(nums)
        if k>l:
            k=k%l
        nums[:] = list(reversed(nums[:]))    #reversed返回值是迭代器，要转换格式
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])


#这种方法没有上一种快。好吧又交了一边差不多，，，

