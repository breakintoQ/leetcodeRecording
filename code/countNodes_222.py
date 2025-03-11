# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        else:
            right=left=0
            left  += self.countNodes(root.left)
            right += self.countNodes(root.right)
            return left+right+1
        
#看了眼题解复杂度较低的方法是先找层数，然后可以判断节点个数区间，然后可以开始二分找
#感觉不是我能想出来的方法，略过了。