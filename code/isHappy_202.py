class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {}  # 使用字典存储出现过的数字
        
        while n != 1:
            n = sum(int(digit) ** 2 for digit in str(n))  # 计算平方和
            
            if n in seen:  # 如果 n 已经出现过，说明进入循环
                return False
            
            seen[n] = True  # 将 n 存入字典
        
        return True  # n 变成 1，返回 True


# 这道题的重点是找规律，其规律为若进入循环，则证明不是快乐数，跳出即可。进入循环即字典中已有该键出现
# 因为只有这两种情况。