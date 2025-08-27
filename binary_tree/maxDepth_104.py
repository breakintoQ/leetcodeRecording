class Solution:
    def maxDepth(self, root) ->int:
        if root is None: 
            return 0 
        else: 
            left_height = self.maxDepth(root.left) 
            right_height = self.maxDepth(root.right) 
            return max(left_height, right_height) + 1 

# 深搜。基础深搜。今天没动脑子直接复制的，学习方法，都忘了已经
# 今天结束了，过生日奖励自己歇逼（
# 明天把树相关仔细看看



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            else:
                left = 1+dfs(root.left)
                right = 1+dfs(root.right)
                
                return max(left,right)
        
        return dfs(root)