# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        
        curr = head

        while head and curr.next is not None:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return head