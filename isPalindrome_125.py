class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        ptr1 = 0
        ptr2 = l-1
        while ptr1<ptr2:
            while ptr1<ptr2 and not s[ptr1].isalnum() :
                ptr1+=1
            while ptr1<ptr2 and not s[ptr2].isalnum():
                ptr2-=1
            if s[ptr1].lower()==s[ptr2].lower():
                ptr1+=1
                ptr2-=1
                continue
            else:
                return False
            
        return True

        # re.match(r'[A-Za-z0-9]',s[ptr1]) 正则表达式判断字母数字号 
        # 所有方法调用记得加括号，才可被视为方法调用。否则被视为方法对象
        #方法对象适用于就取方法本身时，把他当作一个普通的对象使用
        #方法调用适用于执行方法并取其返回值时。