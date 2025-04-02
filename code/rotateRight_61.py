# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         temp= []
#         count = 0
#         copy =head
#         while copy:
#             count+=1
#             temp.append(copy.val)
#             copy = copy.next

#         k = k%count
#         if k == 0:
#             return head
        
#         temp[:count-k].reverse()
#         temp[count-k:].reverse()
#         temp[:].reverse()

#         cnt = head
#         i=0
#         while cnt:
#             cnt.val = temp[i]
#             i+=1
#             cnt=cnt.next
#         return head


#转数组不行，使用链表

from typing import Optional

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # 1. 计算链表长度，并找到链表的尾节点
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # 2. 计算实际需要旋转的步数
        k = k % length
        if k == 0:
            return head

        # 3. 找到新的尾节点（倒数第 k+1 个节点）
        new_tail_position = length - k
        new_tail = head
        for _ in range(new_tail_position - 1):
            new_tail = new_tail.next

        # 4. 更新链表结构
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head

        return new_head
        
