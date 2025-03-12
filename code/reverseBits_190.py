class Solution:
    def reverseBits(self, n: int) -> int:
        # 将整数转换为32位二进制字符串
        binary_str = bin(n)[2:].zfill(32)
        # 反转二进制字符串
        reversed_str = binary_str[::-1]  #反向遍历
        # 将反转后的二进制字符串转换回整数
        return int(reversed_str, 2)