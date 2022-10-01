# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        m = {}
        self.traverseTree(root, root, m)
        
        while m[p] is not m[q]:
            
            # special case:
            if (m[p] is q):
                return q
            elif (m[q] is p):
                return p
            
            # using binary tree to advantage
            # if m[p] < q:
                
            
            p = m[p]
            q = m[q]
            
        # or m[q]
        return m[p]
        
    def traverseTree(self, prev, root, m):
        
        m[root] = prev
        
        if not(root.left is None and root.right is None):
            
            if root.left:
                self.traverseTree(root, root.left, m)
                
            if root.right:
                self.traverseTree(root, root.right, m)
        
             
        
            