# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessthan = ListNode(0)
        head_lessthan = lessthan
        morethan = ListNode(0)
        head_morethan = morethan
        while head:
            if head.val<x:
                lessthan.next = head
                head = head.next
                lessthan = lessthan.next
            else:
                morethan.next = head
                head = head.next
                morethan = morethan.next
        morethan.next = None
        lessthan.next = head_morethan.next
        return head_lessthan.next
        