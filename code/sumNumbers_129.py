

from typing import Optional

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], current_sum: int) -> int:
            if not node:
                return 0

            # 更新当前路径的数字
            current_sum = current_sum * 10 + node.val #这步算的是一条路径上的和

            # 如果是叶子节点，返回当前路径的数字
            if not node.left and not node.right:
                return current_sum

            # 递归处理左右子树，并返回它们的和
            left_sum = dfs(node.left, current_sum)
            right_sum = dfs(node.right, current_sum)
            return left_sum + right_sum   #这步算的是所有路径和相加

        # 从根节点开始递归
        return dfs(root, 0)