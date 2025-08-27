# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = ListNode(-1)
        result = head
        while list1 != None and list2 != None:
            if list1.val>=list2.val:
                result.next = list2
                list2 = list2.next
            else:
                result.next = list1
                list1 = list1.next
            result =result.next

        if list1!=None:
            result.next = list1
        if list2!= None:
            result.next = list2
        return head.next
    
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         prehead = ListNode(-1)   初始化一个值为-1的节点

#         prev = prehead
#         while l1 and l2:
#             if l1.val <= l2.val:
#                 prev.next = l1
#                 l1 = l1.next
#             else:
#                 prev.next = l2
#                 l2 = l2.next            
#             prev = prev.next

#         # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
#         prev.next = l1 if l1 is not None else l2

#         return prehead.next



#注释是官方题解，自己没写出来。感觉迭代的更容易理解一点。跟我思路基本一致，但是我卡在没设头节点了
#还是不熟悉导致的，以后会更容易




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(-1)
        dummy = ListNode(-1)
        
        prev.next = dummy

        while list1 and list2:
            if list1.val>=list2.val:
                cnt = ListNode(list2.val)
                dummy.next = cnt
                dummy = dummy.next
                list2 = list2.next
            else:
                cnt = ListNode(list1.val)
                dummy.next = cnt
                dummy = dummy.next
                list1 = list1.next
        
        if not list1 and list2:
            dummy.next=list2
        elif not list2 and list1:
            dummy.next = list1

        return prev.next.next