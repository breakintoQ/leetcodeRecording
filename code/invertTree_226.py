# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None :
            return root
        # elif root.right is None and root.left is None:
        #     return root       #这个判断语句不必要
        else:
            root_left = self.invertTree(root.left)
            root_right = self.invertTree(root.right)
            root.left = root_right
            root.right = root_left
            return root
        
#一遍过爽呀