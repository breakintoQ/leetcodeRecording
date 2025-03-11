# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        averages = list()
        queue = collections.deque([root])  #root加入队列
        while queue:
            total = 0   #用于累加当前层所有节点的值
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()  #弹出最左节点（最先放入的节点）
                total += node.val
                left, right = node.left, node.right
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
            averages.append(total / size)
        return averages


#层序遍历已经忘了，隐约记得是写到数组里
#用bfs简单一点，，给出的解答是官方bfs。bfs我已经完全忘了。py里到目前为止还没用过队列，学习一下。
#已经完全忘了bfs，也就是压进队列然后分别把左右节点压进队列，恩
#层序用bfs好用点