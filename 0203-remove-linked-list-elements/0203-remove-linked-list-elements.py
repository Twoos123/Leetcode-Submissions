# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        while head and head.val == val:
            head = head.next
        
        curr, prev = head, None
        res = head

        while curr:
            if curr.val == val:
                if prev:
                    prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next
        return res