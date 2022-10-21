# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        def traverse(node, lst):
            
            if node is None:
                return lst
            else:
                
                lst = traverse(node.left, lst)
                lst = traverse(node.right, lst)
                lst += [node.val]
                
                return lst
                
        return traverse(root, [])