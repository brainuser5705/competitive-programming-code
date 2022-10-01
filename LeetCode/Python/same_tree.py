# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        if p is None and q is None:
            return True
        elif ((p is None) ^ (q is None)) or (p.val != q.val):
            return False
        else:
            if p.left == None and q.left == None and p.right == None and q.right == None: # is leaf node
                return True
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
            