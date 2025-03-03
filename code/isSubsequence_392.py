class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #判断s为t的子序列
        l1 = len(s)
        l2 = len(t)
        ptr1 = 0
        ptr2 = 0
        if l1 == 0:
            return True
        if l2 == 0:
            return False
        while ptr2 < l2 and ptr1 < l1:
            if s[ptr1]==t[ptr2]:
                ptr1+=1
                ptr2+=1
                continue
            else:
                 ptr2+=1
        if ptr1 == l1:
            return True
        else:
            return False
        
#用例中发现的错误：循环判断条件出错。两个数组都要判断不然会越界。p2循环结束非字串，p1是子串
#判断条件忽略了只要相同就前移动，所以ptr1结束时一定已经是数组末尾角标又加一了。