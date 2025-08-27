class Solution:
    def removeDuplicates(self, s: str) -> str:
        l = len(s)
        i=1
        result = s[0]
        while i<l:
            result+=s[i]
            if len(result)>=2 and result[-1]==result[-2]:
                result = result[:-2]
            i+=1
        return result
    
solution = Solution()
print(solution.removeDuplicates("abbaca"))

# class Solution:
#     def removeDuplicates(self, s: str) -> str:
#       stack = []
#       for char in s:
#         if stack and stack[-1] == char:
#           stack.pop()
#         else:
#           stack.append(char)
#       return ''.join(stack)


#用list转str，pop快。但是内存消耗大
#重新记忆join
