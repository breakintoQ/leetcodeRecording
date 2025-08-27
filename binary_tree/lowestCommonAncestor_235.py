# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#二叉搜索树，当常规写如下：
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or p == root or q == root:
            return root
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if left and right:
            return root
        
        else:
            return left if left else right
        


#使用二叉搜索树性质：
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or (p.val < root.val and q.val>root.val) or(p.val>root.val and q.val<root.val):
            return root
        
        elif p.val == root.val:
            return p
        
        elif q.val == root.val:
            return q
        
        elif p.val >root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        
        elif p.val <root.val and q.val <root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        
#咋又一次过了，我是二叉搜索树之神

