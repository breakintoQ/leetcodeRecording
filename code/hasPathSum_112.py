# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        elif not root.left and not root.right:
            return root.val == targetSum
        else:
            left = self.hasPathSum(root.left,targetSum-root.val)
            right = self.hasPathSum(root.right,targetSum-root.val)
            return left or right
        
#判题判了好长时间吓死我了以为挂了原来是服务器炸了哈哈你看这事闹得