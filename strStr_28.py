class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0,len(haystack)-len(needle)+1): #最后一个可能的起始位置不会超出 haystack 的长度
            if haystack[i:i+len(needle)] == needle:  #因为这里在加,记住py不用一个一个比
                return i
        return -1

# kmp两门课看了两遍都是只会思路还看了就忘，嗯啊。暴力到死了属于
# 这个是官方的暴力，学习一下尽量少的代码解决。
# 我自己写又得又臭又长了