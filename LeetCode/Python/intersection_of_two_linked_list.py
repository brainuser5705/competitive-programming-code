class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    
        # make a list of all the nodes for one head
        nodes = []
        curr = headA
        while (curr != None):
            nodes.append(curr)
            curr = curr.next
        
        # go through it with the second head and see if any of the nodes is in the list
        curr = headB
        while (curr != None and curr not in nodes):
            curr = curr.next
            
        return curr


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    
        
        # get the len of both lists
        
        lenA = 0
        lenB = 0
        
        curr = headA
        while (curr != None):
            lenA += 1
            curr = curr.next
            
        curr = headB
        while (curr != None):
            lenB += 1
            curr = curr.next
            
            
        # find the min and max list
        
        minLen = min(lenA, lenB)
        maxLen = max(lenA, lenB)
        
        if (lenA == minLen):
            minList = headA
            maxList = headB
        else:
            minList = headB
            maxList = headA
            
        # "trim down" the max list so that it is the same length as the min len
        for i in range(maxLen - minLen):
            maxList = maxList.next
            
        # compare the node one by one until intersection or end is encountered
        while(minList != None and maxList != None and minList != maxList):
            minList = minList.next
            maxList = maxList.next
            
        return minList

# wtf...
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode | None:
        curA, curB = headA, headB

        while curA != curB:
            curA = curA.next if curA else headB
            curB = curB.next if curB else headA

        return curA