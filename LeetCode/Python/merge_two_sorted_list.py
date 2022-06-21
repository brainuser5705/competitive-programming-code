# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        head = None
        cur = None
        
        while list1 != None and list2 != None:
            
            val = None
            if list1.val < list2.val:
                val = list1
                list1 = list1.next
            else:
                val = list2
                list2 = list2.next
                
            if head == None:
                cur = val
                head = cur
            else:
                cur.next = val
                cur = cur.next
                
        if list1 != None:
            if head == None:
                head = list1
            else:
                cur.next = list1
            
        if list2 != None:
            if head == None:
                head = list2
            else:
                cur.next = list2
                     
        return head
                
            
                
        
        