class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        length = len(nums)
        p = length-1
        if len == 0:
            return 0
        else:
            for i in range(0,length,1):
                if nums[i] ==val:
                    k+=1
                    while(1):
                        if p>i:
                            if  nums[p]!= val:
                                nums[i] = nums[p]
                                p-=1
                                break
                            else:
                                p-=1
                        else:
                            break
                        
            return length-k            
        
        """
        又是学python语法的一天哈哈。我们都喜欢的.len在py里居然是没有的，绷不住。
        但是自己写出来了跟官方解不一样的，爽。虽然差的也不多都是正反双指针。我的还是有点丑，但是随便吧。
        """