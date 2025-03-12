class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for num in nums:  # 1. 遍历 nums 执行异或运算
            x ^= num      
        return x;         # 2. 返回出现一次的数字 x

#所有位的元素异或，最后留下的是不一样的，且异或满足交换律，顺序无关。
#a ^ a = 0：任何数与自身异或结果为0。
#a ^ 0 = a：任何数与0异或结果为其自身。
#注意：异或是转为二进制逐位进行，因此有上面的性质