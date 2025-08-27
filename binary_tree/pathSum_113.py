# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        path = []
        result = []

        def backtrack(root,cnt_sum):
            if not root:
                return 
            
            path.append(root.val)
            cnt_sum+=root.val

            if not root.left and not root.right and cnt_sum==targetSum:
                result.append(path[:])
            else:
                backtrack(root.left,cnt_sum)
                backtrack(root.right,cnt_sum)
            path.pop()

        
        backtrack(root,0)
        return result