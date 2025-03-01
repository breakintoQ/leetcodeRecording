import re
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        space_list = [i.start() for i in re.finditer(" ",s)] #不记也没事不如自己写遍历
        l=len(space_list)
        length = len(s)
        flag=0
        if l == 0:
            return length
        elif space_list[l-1] == length-1:
            for i in range (l-1, 0 , -1):
                if space_list[i]-space_list[i-1]!=1:
                    flag = 1
                    k = i
                    break
            if flag ==1 :
                return space_list[k]-space_list[k-1]-1
            else:
                return space_list[0]
                
        else:
            return (length-1)-space_list[l-1]
        
# java很简单，py不知道有没有对应库。哎呀想复杂了，应该直接查字母不应该查空格，空格情况太多了