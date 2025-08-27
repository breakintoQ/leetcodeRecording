#中序，递归

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(root):
            if root:
                if root.left:
                    dfs(root.left)
                
                result.append(root.val)

                if root.right:
                    dfs(root.right)


        dfs(root)
        return result
    

#迭代：

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        cnt = root

        while cnt or stack:
            while cnt:
                stack.append(cnt)
                cnt = cnt.left
            
            cnt = stack.pop()
            result.append(cnt.val)

            cnt = cnt.right
        
        return result

            