# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        copy = head
        while copy:
            count+=1
            copy = copy.next
        k = count - n
        cnt = head
        if n!=1 and k !=0:
            for _ in range(k-1):
                cnt = cnt.next
            cnt.next = cnt.next.next  
        elif n!=1 and k == 0:
            return head.next
        elif n ==1 and count!=1:
            while cnt.next.next:
                cnt = cnt.next
            cnt.next = None
        else:
            return None
        return head


#不知道简单做法怎么做只知道我这样分类讨论很笨（，，
#以下是双指针法:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# from typing import Optional

# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         # 创建一个哑节点，指向链表头部
#         dummy = ListNode(0)
#         dummy.next = head
#         fast = dummy
#         slow = dummy

#         # 1. 让 fast 指针先向前移动 n+1 步
#         for _ in range(n + 1):
#             fast = fast.next

#         # 2. 同时移动 fast 和 slow，直到 fast 到达链表末尾
#         while fast:
#             fast = fast.next
#             slow = slow.next

#         # 3. 删除倒数第 n 个节点
#         slow.next = slow.next.next

#         # 返回链表头节点
#         return dummy.next