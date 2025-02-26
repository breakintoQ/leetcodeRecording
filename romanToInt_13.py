class Solution:
    def romanToInt(self, s: str) -> int:
        SYMBOL_VALUES = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    } #用一个字典来进行键值替换
        ans = 0
        n = len(s)
        for i, ch in enumerate(s):  #enumerate作用：同时获取索引和值
            value = SYMBOL_VALUES[ch]
            if i < n - 1 and value < SYMBOL_VALUES[s[i + 1]]:
                ans -= value
            else:
                ans += value
        return ans

"""
字典使用练习了属于。数据结构熟就不难，明天再练一次
今天写的三道题都有再看看的必要，哎，语法还是太不熟悉了。很多基础库函数都不太会用，不行先学一下
"""