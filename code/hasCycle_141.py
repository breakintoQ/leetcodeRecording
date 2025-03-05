class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

#不考虑复杂度就没有难度直接遍历的一道题，如果重复出现就返回正确。但是没看懂提示语，原来他的意思是告诉我内部定义的类怎么样，，