# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#思路简单，但是两重递归，很慢
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root :
            return True
        
        def dfs(root):
            if not root:
                return 0
            
            left = 1+dfs(root.left)
            right = 1+dfs(root.right)

            return max(left,right)
        

        if abs(dfs(root.left)-dfs(root.right))>1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

#后序，返回高度和是否平衡两个值
from typing import Optional

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkBalance(node):
            """
            返回 (是否平衡, 高度)
            如果不平衡，高度返回 -1
            """
            if not node:
                return True, 0
            
            # 检查左子树
            left_balanced, left_height = checkBalance(node.left)
            if not left_balanced:
                return False, -1
            
            # 检查右子树
            right_balanced, right_height = checkBalance(node.right)
            if not right_balanced:
                return False, -1
            
            # 检查当前节点是否平衡
            if abs(left_height - right_height) > 1:
                return False, -1
            
            # 返回当前节点的平衡状态和高度
            return True, 1 + max(left_height, right_height)
        
        balanced, _ = checkBalance(root)
        return balanced