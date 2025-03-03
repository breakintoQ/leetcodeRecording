class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        l1 = len(s)
        l2 = len(t)
        if l1!=l2:
            return False
        ptr1 = 0
        ptr2 = 0
        while ptr1<l1 and ptr2 <l2:
            if (s[ptr1] in map1 and map1[s[ptr1]]!=t[ptr2]) or (t[ptr2] in map2 and map2[t[ptr2]]!=s[ptr1]):
                    return False
            else:
                map1[s[ptr1]]=t[ptr2]
                map2[t[ptr2]]=s[ptr1]
                ptr1+=1
                ptr2+=1
        return True
        
#虽然只有一重循环但是时间莫名其妙的慢啊，真的很慢，奇怪之。
#虽然是看了题解才写的但是应该说难度不算大，自己建立映射就好了
#要注意是双向的映射
                