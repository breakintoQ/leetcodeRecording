"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 创建一个哈希表，用于存储原节点到新节点的映射
        old_to_new = {}

        # 第一遍遍历：复制所有节点，并存储在哈希表中
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        # 第二遍遍历：设置新节点的 next 和 random 指针
        current = head
        while current:
            if current.next:
                old_to_new[current].next = old_to_new[current.next]
            if current.random:
                old_to_new[current].random = old_to_new[current.random]
            current = current.next

        # 返回新链表的头节点
        return old_to_new[head]
    
#链表深拷贝，发人深省啊发人深省
#用哈希表的题除了标在哈希表区的都没做对过，字典这给地方情况太复杂了