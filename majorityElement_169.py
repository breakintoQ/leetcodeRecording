class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        flag:dict = {}
        for i in range (0,n,1):
            flag[nums[i]]=0
        for i in range (0,n,1):
            flag[nums[i]]+=1
        length = len(list(flag))
        for i in range (0,length,1):
            record_key = list(flag.keys())[i]
            record_value = flag[record_key]
            if record_value > n/2:
                return record_key
            else:
                continue
        return 0
    

    """
    class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
    这是官方给的。我喷了呀，又学习内部库函数了家人们。暴力思路两个O(n),没啥可说，纯学数据结构了属于。思路超级简单超级暴力。
    剩下官方解可以看但是我觉得我必定想不出来，嗯啊，小时候上的课都已经就饭吃了
    
    """