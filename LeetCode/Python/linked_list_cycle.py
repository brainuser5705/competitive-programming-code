# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev_nodes = []
        
        curr = head
        while curr is not None:
            if curr in prev_nodes:
                return curr
            prev_nodes.append(curr)
            curr = curr.next
            
        return None