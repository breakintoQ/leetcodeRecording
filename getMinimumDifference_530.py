# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def getMinimumDifference(self, root: TreeNode) -> int:
#         queue = collections.deque([root])
#         minimum = float('inf')
#         while queue:
#             size = len(queue)
#             for _ in range(size):
#                 node = queue.popleft()
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
                

            
# 没写出来。二叉搜索树的性质已经不记得了。
# 二叉搜索树中序遍历得到的值序列是递增有序的。因此中序遍历之后得到的序列可以直接比较。
#下面是正确解：


class Solution:
    pre = float('-inf')  # 初始化前一个节点的值为负无穷大

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return float('inf')  # 如果当前节点为空，返回正无穷大，表示没有差值

        # 递归计算左子树的最小差值
        res = self.getMinimumDifference(root.left)

        # 更新当前节点与前一个节点值的差值，并取最小值
        res = min(res, abs(root.val - self.pre))

        # 更新前一个节点的值为当前节点的值
        self.pre = root.val

        # 递归计算右子树的最小差值，并返回最终的最小差值
        return min(res, self.getMinimumDifference(root.right))


#这块不算熟，bfs和搜索树都不熟。合着就前序dfs熟，嗯啊。
#后续重点刷。