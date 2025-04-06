# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from typing import List,Optional

    result = []

    def dfs (self, root: Optional[TreeNode]) -> None:
        if not root:
            return 
        else:
            self.result.append(root.val)
            self.dfs(root.left)
            self.dfs(root.right)
            return root


    def flatten(self, root: Optional[TreeNode]) -> None:
            if not root or (not root.right and not root.left):
                 return
            else:
                self.dfs(root)
                # l = len(self.result)
                # for i in range(1,l):
                #     root.left = None
                #     root.right = TreeNode(self.result[i])
                #     root = root.right
                current = root
                current.val = self.result[0]
                for i in range(1, len(self.result)):
                    current.left = None
                    current.right = TreeNode(self.result[i])
                    current = current.right

                #这里改current，因为不知道为什么在力扣测试里有直接用root之前的值一直被缓存无法清除

#原地修改的办法：
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from typing import Optional

# class Solution:
#     def flatten(self, root: Optional[TreeNode]) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         if not root:
#             return

#         # 使用一个变量记录上一个访问的节点
#         self.prev = None

#         def dfs(node: Optional[TreeNode]):
#             if not node:
#                 return

#             # 后序遍历：先处理右子树，再处理左子树
#             dfs(node.right)
#             dfs(node.left)

#             # 修改当前节点的结构
#             node.right = self.prev
#             node.left = None
#             self.prev = node

#         dfs(root)