class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict1={}
        for key,value in enumerate(nums):
            if value not in dict1:
                dict1[value] = [key]
            else:
                dict1[value].append(key)
        for i in dict1.values():
            if len(i)>1:
                for s in range(0,len(i),1):
                    for t in range (s+1,len(i),1):
                        if abs(i[s]-i[t])<= k:
                            return True
                        
        return False

# 可以使用哈希表记录每个元素的最大下标。从左到右遍历数组 nums，当遍历到下标 i 时，进行如下操作：
# 如果哈希表中已经存在和 nums[i] 相等的元素且该元素在哈希表中记录的下标 j 满足 i−j≤k，返回 true；
# 将 nums[i] 和下标 i 存入哈希表，此时 i 是 nums[i] 的最大下标。
# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         pos = {}
#         for i, num in enumerate(nums):
#             if num in pos and i - pos[num] <= k:
#                 return True
#             pos[num] = i
#         return False
#喷了，不动脑子写的三重循环写完不敢交，居然过了，嗯啊，但是复杂度太高了。想复杂了属于，直接比就好了，不用在循环。