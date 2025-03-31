# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r1 = 0
        r2 = 0
        i = 0
        while l1:
            r1 += l1.val*(10**i)
            i+=1
            l1 = l1.next
        i = 0 
        while l2 :
            r2 += l2.val*(10**i)
            i+=1
            l2 = l2.next

        r3 = r1+r2
        result = ListNode()
        cnt = result
        while r3 !=0 :
            cnt.val = r3%10
            r3 //=10
            if r3 !=0:
                cnt.next = ListNode()
                cnt = cnt.next
        return result