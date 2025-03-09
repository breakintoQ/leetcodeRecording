# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if root is None:
#             return True
#         elif root.left is not None and root.right is None:
#             return False
#         elif root.left is None and root.right is not None:
#             return False
#         else:
#             left = self.isSymmetric(root.left)
#             right = self.isSymmetric(root.right)
#             return left and right



#不对，想简单了。不是左右子树一致是轴对称。


class Solution:  #递归
    def check(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.check(p.left, q.right) and self.check(p.right, q.left)
    #三个条件：根相同，左子树的左和右子树的右对称，左子树的右和右子树的左对称

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.check(root.left, root.right)
    
    #这个要再看，感觉很奇怪的做法。仔细想想又不奇怪。嗯啊。左子树的左和右子树的右以及左子树的右和右子树的左都应该相同。