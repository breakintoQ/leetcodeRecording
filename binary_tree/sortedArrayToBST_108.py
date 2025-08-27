# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) ->TreeNode:
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            node = TreeNode(nums[0])
            return node
        else:
            nodel = self.sortedArrayToBST(nums[:len(nums)//2])
            node = TreeNode(nums[len(nums)//2])
            node.left =nodel
            noder = self.sortedArrayToBST(nums[len(nums)//2+1:len(nums)])
            node.right = noder
            return node
        

#自己都不敢提交居然过了，牛逼。


