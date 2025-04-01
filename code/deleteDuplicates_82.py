# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return None
#         else:
#             cnt = head
#             while cnt:
#                 while cnt.next.val == cnt.next.next.val:
#                     cnt.next = cnt.next.next.next
#                 cnt = cnt.next
#             return head

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 创建一个哑节点，指向链表头部
        dummy = ListNode(0, head)
        prev = dummy  # 用于追踪不重复节点的前一个节点

        while head:
            # 如果当前节点和下一个节点的值相同，跳过所有重复节点
            if head.next and head.val == head.next.val:
                # 跳过所有值相同的节点
                while head.next and head.val == head.next.val:
                    head = head.next
                # 将 prev 的 next 指向 head 的下一个节点，跳过重复节点
                prev.next = head.next
            else:
                # 如果当前节点不重复，移动 prev 指针
                prev = prev.next
            # 移动 head 指针
            head = head.next

        return dummy.next