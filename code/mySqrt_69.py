class Solution:
    def mySqrt(self, x: int) -> int:
        i=0
        while 1:
            if i*i>x:
                break
            i+=1
        return i-1
    

    #太笨蛋了想的是解出来就行。下面给出二分解决方法:
    # class Solution:
    # def mySqrt(self, x: int) -> int:
    #     l, r, ans = 0, x, -1
    #     while l <= r:
    #         mid = (l + r) // 2
    #         if mid * mid <= x:
    #             ans = mid
    #             l = mid + 1
    #         else:
    #             r = mid - 1
    #     return ans
#哎呀看了一下没快多少还不如我们暴力呢
#希望别出，什么破题