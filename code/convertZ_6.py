# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         l = len(s)
#         p1 = 0
#         p2 = 0
#         martex = []
#         while p1<l and p2<l:
#             martex[p1,0:numRows-1] = s[p2:p2+numRows-1]
#             p2+=numRows
#             for i in range(1,numRows-1):
#                 martex[numRows-1-i,i] = s[p2]
#                 p2+=1
#             p1+=numRows-1
#         return str(martex)

#py没有二重数组的用法不然我觉得我挺对的，，，


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1   #i 表示当前字符应该放在哪一行。 也就是说设立行指针，元素为每行组成的字符串
                          #flag 表示当前方向，初始值为 -1。
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag  #第一行或最后一行，换方向
            i += flag
        return "".join(res)