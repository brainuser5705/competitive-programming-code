# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head != None:
            head_val = head.val
            curr = head.next

            while curr != None and curr.val == head_val:
                curr = curr.next

            if curr != None:
                head.next = curr
                self.deleteDuplicates(curr)
            else:
                head.next = None

        return head