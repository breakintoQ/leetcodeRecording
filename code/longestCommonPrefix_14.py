class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l =len(strs)
        d = min(len(s) for s in strs)
        list_result=""
        flag=0
        if l==1:
            return strs[0]
        else:
            for i in range(0,d,1):
                for j in range(0,l-1,1):
                    if strs[j][i] != strs[j+1][i]:
                        flag=1
                        break
                if flag==0:
                    list_result += (strs[0][i])  #python里字符串添加末尾的办法
                else:
                    break
            return list_result
    
#字符串：
# 字符串是不可变的字符序列。
# 不能直接修改字符串的内容。
# 可以使用 + 操作符或 join 方法来连接字符。

# 数组（列表）：
# 列表是有序的集合，可以包含不同类型的元素。
# 可以通过索引访问和修改元素。
# 尝试访问或赋值一个不存在的索引会引发 IndexError。
# 可以使用 append 方法在列表末尾添加元素，避免索引越界。

# 字典：
# 字典是无序的键值对集合。
# 可以通过键直接访问或赋值。
# 向字典添加新的键值对时，如果键不存在，字典会自动创建这个键。
# 不会因为访问不存在的键而引发索引越界错误，但访问不存在的键会引发 KeyError。

# 强转字符串：''.join(list_result)