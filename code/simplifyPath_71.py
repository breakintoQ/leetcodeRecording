# class Solution:
#     def simplifyPath(self, path: str) -> str:
#          l = len(path)
#          stack = []
#          i = 0
#          while i < l:
#             if not stack:
#                 stack.append(path[i])
#                 i+=1
#                 continue
#             if stack[-1] is '/' and path[i] is '/':
#                 i+=1
#                 continue
#             elif stack[-1] is '.':
#                 stack.pop()
#                 stack.pop()
#                 stack.append(path[i])
#             elif stack[-1] is '..':
#                 stack.pop()
#                 stack.pop()
#                 stack.pop()
#                 stack.pop()
#                 stack.append(path[i])
#             else:
#                 stack.append(path[i])
#             i+=1

#          if stack[-1] is '/':
#              stack.pop()
#          return str(stack[:])
    
# s = Solution()
# path = "/home/"
# result = s.simplifyPath(path)


#..那块整乱了。

class Solution:
    def simplifyPath(self, path: str) -> str:
        names = path.split("/") #直接切割之后最后再加
        stack = list()
        for name in names:
            if name == "..":
                if stack:
                    stack.pop()
            elif name and name != ".":
                stack.append(name)
        return "/" + "/".join(stack)

