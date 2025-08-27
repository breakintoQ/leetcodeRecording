# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        while head and head.next:
            if head.val == head.next.val and head.next.next:
                head.next = head.next.next
            elif head.val == head.next.val and not head.next.next:
                head.next = None
            else:
                head=head.next

        
        return dummy.next