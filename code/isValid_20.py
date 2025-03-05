class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()  #空栈
        for ch in s:
            if ch in pairs:  #遇到的是右括号
                if not stack or stack[len(stack)-1] != pairs[ch]:   #目前空栈或栈顶不匹配(第一个遇到的右括号一定是最后一个放进去的左括号)
                    return False
                stack.pop() #弹出栈顶
            else:    #遇到的是左括号
                stack.append(ch)  #先进后出
        
        return not stack


#第一个用栈的函数。学习其方法。