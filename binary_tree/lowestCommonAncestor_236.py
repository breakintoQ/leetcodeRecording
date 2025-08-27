# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if not root:
#             return None
#         if  p == root:
#             return p
#         elif q == root:
#             return q
#         elif self.lowestCommonAncestor(root.left,p,q)==p and self.lowestCommonAncestor(root.right,p,q) ==q:
#             return root
#         elif self.lowestCommonAncestor(root.left,p,q)==q and self.lowestCommonAncestor(root.right,p,q) ==p:
#             return root


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 递归终止条件
        if not root or root == p or root == q:
            return root
        
        # 在左右子树中寻找 p 和 q
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # 如果左右子树都找到了节点，说明 p 和 q 分别在左右子树，当前节点就是 LCA
        if left and right:
            return root
        
        # 如果只有一边找到了节点，返回找到的那一边
        return left if left else right