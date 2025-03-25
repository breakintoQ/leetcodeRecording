# class Solution:
#     import collections
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         l = len(strs)
#         if len (strs) == 1:
#             return [strs]
#         map_colllection = []
#         for str in strs:
#             map_colllection.append(collctions.Counter(str))
        
#         for i in range(l):
#             for j in range(l):
#                 if map_colllection[i] == map_colllection[j]:


from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        #适用于频繁检查和初始化的地方，也就是说可以为不存在的键创建默认值
        
        for s in strs:
            # 将字符串排序后作为键
            sorted_str = ''.join(sorted(s))
            # 将原字符串添加到对应的键的列表中
            anagrams[sorted_str].append(s)
        
        # 返回字典中所有值的列表
        return list(anagrams.values())