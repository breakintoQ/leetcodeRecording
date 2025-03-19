class Solution:
    def reverseWords(self, s: str) -> str:
        strs1 = s.split()
        strs2 = list(reversed(strs1))
        # s = ''
        # for i in range(len(strs2)):
        #     if i == len(strs2)-1:
        #         s+=strs2[i]
        #     else:
        #         s+=strs2[i]+' '
        # return s
        return ' '.join(strs2)
    
    #记住join用法
    