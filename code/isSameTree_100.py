# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is not None and q is not None and p.val != q.val:
            return False
        elif p is None and q is not None:
            return False
        elif p is not None and q is None:
            return False
        elif p is None and q is None:
            return True
        else:
            is_left = self.isSameTree(p.left,q.left)
            is_rigth = self.isSameTree(p.right,q.right)
            return is_left and is_rigth


#莫名其妙分了很多if分支，不知道是不是有方便一点的方法。
#嗯啊好吧官方题解也这样。
