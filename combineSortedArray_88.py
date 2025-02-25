class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index: int
        index = -1
        for i in range(m,m+n,1):
            if n==0:
                break
            index+=1
            nums1[i] = nums2[index]

        # for i in range(0,m+n,1):
        #     for j in range (1,m+n-i,1):
        #         if nums1[j]<nums1[j-1]:
        #             temp:int 
        #             temp = nums1[j]
        #             nums1[j]=nums1[j-1]
        #             nums1[j-1] = temp
        nums1.sort()

        """
        第一想法是是不是太简单了不敢写，结果真就这么简单的解法1，但是不知道为什么sort不让用还以为是不让用内部库，看官方解应该也可以，不知道为啥。
        小时候学数据结构和算法都用的cpp然后用java导致python语法都现查，太简单了我们python（指语法）
        sort总是通不过于是自己写发现连冒泡都忘了，上学上稀碎了属于。
        看官方解发现反向指针，太巧妙了啊不是，这我咋学。以超绝高的时间复杂度实现了简单的小问题（嗯啊）
        day1.1加油啊绝望的大姐姐
        """