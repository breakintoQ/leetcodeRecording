class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range (0,l,1):
            for j in range (i+1,l,1):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return 0
    

    # 开辟一个新匹配：
    # class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     index={}
    #     for i,j in enumerate(nums):
    #         if target-j in index：
    #             return (index[target-j],i)
    #         index[j]=i        将nums的值作为key，将其原本的index（数组的顺序）作为value   
    #呃就是省时间费空间了，但是双重暴力循环实在是太简单了没忍住，，其实是处在哈希表里的题应该想想的