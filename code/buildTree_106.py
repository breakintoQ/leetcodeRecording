# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        
        root_val = postorder[len(postorder)-1]
        root = TreeNode(root_val)

        root_index = inorder.index(root_val)

        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index+1:]

        left_postorder = postorder[:len(left_inorder)]
        right_postorder = postorder[len(left_inorder):len(postorder)-1]

        root.left = self.buildTree(left_inorder,left_postorder)
        root.right = self.buildTree(right_inorder,right_postorder)

        return root