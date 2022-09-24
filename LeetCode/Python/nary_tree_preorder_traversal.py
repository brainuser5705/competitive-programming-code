"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        l = []
        
        # if the node exists, add it to the list
        if root != None:
            l  += [root.val]
        
            # if the node has children, go through them recursively
            if (root.children != None):
                for child in root.children:
                    # append its return to the current list
                    l = l + self.preorder(child)
        
        return l