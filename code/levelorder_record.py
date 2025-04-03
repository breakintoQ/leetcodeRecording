from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []  # 用于存储每一层的节点值
        queue = deque([root])  # 初始化队列，将根节点加入队列

        while queue:
            level = []  # 存储当前层的节点值
            size = len(queue)  # 当前层的节点数量

            for _ in range(size):
                node = queue.popleft()  # 弹出队列中的节点
                level.append(node.val)  # 将节点值加入当前层

                # 将左右子节点加入队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)  # 将当前层的节点值加入结果

        return result
    
    #层序遍历二叉树（字节笔试）