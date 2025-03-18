class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.indices = {}
        # 变长数组中存储元素，哈希表中存储每个元素在变长数组中的下标。哈希表下标为数组中的值，值为在数组中的下标

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.indices[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        id = self.indices[val]
        self.nums[id] = self.nums[-1]  #在这一步用最后一个值覆盖被删除的元素
        self.indices[self.nums[id]] = id  #因为上一步更新了，所以相当于原来的最后一个值的索引更新了，更新为id现在的位置
        self.nums.pop()  #把最后一个弹出
        del self.indices[val]  #删除哈希表中的val项
        return True

    def getRandom(self) -> int:
        return choice(self.nums)

    

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()