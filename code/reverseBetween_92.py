# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
 # 创建一个哑节点，便于处理头节点的特殊情况
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # 1. 移动 prev 到 left 的前一个节点
        for _ in range(left - 1):
            prev = prev.next

        # 2. 开始反转链表
        current = prev.next
        next_node = None
# current 指向当前正在处理的节点。
# next_node 用于保存 current.next，即下一个需要反转的节点。
# 通过调整指针，将 next_node 插入到 prev 和 current 之间。
        for _ in range(right - left):
            next_node = current.next
            #将next_node摘出去
            current.next = next_node.next
            #将next_node指向反转部分的头部
            next_node.next = prev.next
            #将 next_node 插入到反转部分的最前面
            prev.next = next_node

        return dummy.next

#这个要看