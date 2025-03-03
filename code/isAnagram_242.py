import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = collections.Counter(s)
        map2 = collections.Counter(t)

        if map1 == map2:
            return True
        else:
            return False
        
#即将成为调包大师