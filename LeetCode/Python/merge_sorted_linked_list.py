# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            val1 = list1.val
            val2 = list2.val

            if val1 < val2:
                list1.next = self.mergeTwoLists(list1.next,list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list2.next, list1)
                return list2