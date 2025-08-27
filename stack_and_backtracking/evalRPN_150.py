# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         l = len(tokens)
#         stack = []
#         i = 0
#         for token in tokens:
#             if token not in {"+", "-", "*", "/"}:
#                 token = int (token)    #这里不好解决，没办法这么赋值
#         while i<l:
#             stack.append(tokens[i])
#             if stack[-1] == '+':
#                 result = 0
#                 for _ in range(2):
#                     stack.pop()
#                     result+=stack[-1]
#                 stack.pop()
#                 stack.append(result)
#             elif stack[-1] == '-':
#                 stack.pop()
#                 result = stack[-1]
#                 stack.pop()
#                 result -=stack[-1]
#                 stack.pop()
#                 stack.append(-result)
#             elif stack[-1] == '*':
#                 result = 1
#                 for _ in range(2):
#                     stack.pop()
#                     result*=stack[-1]
#                 stack.pop()
#                 stack.append(result)
#             elif stack[-1] == '/':
#                 stack.pop()
#                 k1 = stack[-1]
#                 stack.pop()
#                 k2 = stack[-1]
#                 stack.pop()
#                 stack.append(k2/k1)
#             i+=1
#         return stack[-1]
    

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            # 判断是否为数字
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))  # 将数字压入栈
            else:
                # 如果是操作符，弹出栈顶的两个数字进行计算
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # 注意 Python 的整数除法需要向零截断
                    stack.append(int(a / b))
        
        return stack[-1]
    


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range (len(tokens)):
            if tokens[i] not in {"+","-","*","/"}:
                stack.append(int(tokens[i]))
            elif tokens[i] == "+":
                temp = stack[-1]+stack[-2]
                stack.pop()
                stack.pop()
                stack.append(temp)
            elif tokens[i] == "-":
                temp = stack[-2]-stack[-1]
                stack.pop()
                stack.pop()
                stack.append(temp)
            elif tokens[i] == "*":
                temp = stack[-2]*stack[-1]
                stack.pop()
                stack.pop()
                stack.append(temp)
            elif tokens[i] == "/":
                temp = int(stack[-2] / stack[-1])
                stack.pop()
                stack.pop()
                stack.append(temp)
        
        return int(stack[-1])