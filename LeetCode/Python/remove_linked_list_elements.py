# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        final = None
        
        prev = None
        curr = head
        
        while curr != None:
            
            if curr.val == val:
                # skip it
                if prev is not None:    # needed after the first pass
                    prev.next = curr.next
                # reassign curr (keep the same prev)
                curr = curr.next
            else:
                if final is None: # assign the return value (head)
                    final = curr
                prev = curr
                curr = curr.next
                    
        return final