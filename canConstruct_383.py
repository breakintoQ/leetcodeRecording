class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # if len(ransomNote) > len(magazine):
        #     return False
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

#读题读了好久没看懂需求啊，不知道是一定要按顺序排放还是怎么的，打眼一看跟字符串识别差不多了。给的用例也不好
#先看解才明白原来是一个字母只能用一次，最后看magazine里的文字能不能组合为ransomnote里的文字的意思。
#理解意思就好做多了，只要m里每个字母出现的次数都多于r就可以了。
#py库还是很好用的。
#官方题解里被我注释掉的两行完全没用啊，一行调库解决了。
#直接相减很有意思。该对象只包含那些在 ransomNote 中但不在 magazine 中的元素及其计数。与m比r多的那部分没关系
#用not相当于直接提取了对错值，不会出现真的相减之后出现的字典。