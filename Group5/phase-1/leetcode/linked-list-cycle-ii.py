# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        checker = set()
        length = 0 
        cur = head
        while cur :
            if cur in checker:
                return cur 
            else:
                checker.add(cur)
                
            cur = cur.next
        return None