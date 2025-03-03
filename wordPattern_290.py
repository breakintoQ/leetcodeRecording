class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        w =s.split()
        map1 = {}
        map2 = {}
        l1 = len(pattern)
        l2 = len(w)
        if l1!=l2:
            return False
        ptr1 = 0
        ptr2 = 0
        while ptr1<l1 and ptr2 <l2:
            if (pattern[ptr1] in map1 and map1[pattern[ptr1]]!=w[ptr2]) or (w[ptr2] in map2 and map2[w[ptr2]]!=pattern[ptr1]):
                    return False
            else:
                map1[pattern[ptr1]]=w[ptr2]
                map2[w[ptr2]]=pattern[ptr1]
                ptr1+=1
                ptr2+=1
        return True
    
    #跟上题完全一模一样啊（205），用split分割一下就好了，五分钟解决。