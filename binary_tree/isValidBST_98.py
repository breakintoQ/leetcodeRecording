# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#最简单的思路就是中序遍历后看是否有序，嗯，但是我先试试不这么写,但是失败了，，，试试我最一开始的
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root,max_val,min_val):
            if not root:
                return True
            
            if not root.left and not root.right:
                return True
            
            if root.left and root.val <= root.left.val:
                return False
            
            if root.right and root.val >= root.right.val:
                return False
            
            return dfs(root.left,min_val,root.val) and dfs(root.right,root.val,max_val)
        return dfs(root,float('-inf'),float('inf'))

#全排序可能碰到的问题是可能有重复数
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = []

        def dfs(root):
            if root:
                if root.left:
                    dfs(root.left)
                
                result.append(root.val)

                if root.right:
                    dfs(root.right)
        dfs(root)

        for i in range(1,len(result)):
            if result[i-1]>=result[i]:
                return False
            
        return True


#正确递归写法，要给一个约束范围
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val, max_val):
            # 空节点是有效的
            if not node:
                return True
            
            # 检查当前节点是否在有效范围内
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # 递归检查左右子树
            # 左子树：上界更新为当前节点值
            # 右子树：下界更新为当前节点值
            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))
        
        return validate(root, float('-inf'), float('inf'))
    


