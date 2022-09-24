# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head
        
        tail = head
        while tail.next is not None:
            new_head = tail.next
            tail.next = new_head.next
            new_head.next = head
            head = new_head
            
        return head