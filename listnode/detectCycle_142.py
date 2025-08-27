# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#哈希表法
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()

        p1 = head

        



#快慢指针法，推导结果是头结点到环入口距离等于相遇点返回环入口距离
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 阶段一：判断是否有环并找到相遇点
        slow, fast = head, head
        meet_node = None
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                meet_node = slow
                break
        
        # 如果 meet_node 为 None，说明 fast 走到了尽头，无环
        if not meet_node:
            return None
            
        # 阶段二：从相遇点找到环的入口
        # 创建一个新指针从头开始
        ptr = head
        
        # 同时移动新指针和慢指针，直到它们相遇
        # 相遇点就是环的入口
        while ptr != meet_node:
            ptr = ptr.next
            meet_node = meet_node.next
            
        return ptr