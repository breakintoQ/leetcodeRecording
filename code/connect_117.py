# """
# # Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next
# """

# import collections
# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
    
#         if not root:
#             return root
#         queue = collections.deque([root])

#         while queue:
#             cnt = queue.popleft()
#             if queue:
#                 if cnt.left:
#                     queue[-1].next = cnt.left
#                 elif cnt.right and not cnt.left:
#                     queue[-1].next = cnt.right
            
#             if cnt.left and cnt.right:
#                 cnt.left.next = cnt.right
#                 queue.append(cnt.left)
#                 queue.append(cnt.right)
#             elif cnt.left and not cnt.right:
#                 queue.append(cnt.left)
#             elif cnt.right and not cnt.left:
#                 queue.append(cnt.right)     

#             return root
        
import collections

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        # 使用队列进行层序遍历
        queue = collections.deque([root])

        while queue:
            size = len(queue)  # 当前层的节点数量
            prev = None  # 用于记录前一个节点

            for _ in range(size):
                # 取出当前层的节点
                node = queue.popleft()

                # 将前一个节点的 next 指向当前节点
                if prev:
                    prev.next = node
                prev = node

                # 将左右子节点加入队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # 当前层的最后一个节点的 next 指针应为 None
            if prev:
                prev.next = None

        return root


