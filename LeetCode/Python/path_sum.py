# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
        # special case
        if root is None:
            return False
        
        else:
            
            # separating the special case conditional check
            # speeds up the code
            return self.recursiveCall(root, targetSum)
        
        
    def recursiveCall(self, root, targetSum):
        
        # leaf node
        if (root.left is None) and (root.right is None):
            # check if its value is the only left
            return root.val == targetSum

        else:
            # recursively do the same for left node (if there is one) and right node (if there is one)
            # make sure to reduce the targetSum by the current node val
            return (root.left and self.hasPathSum(root.left, targetSum-root.val)) or \
                    (root.right and self.hasPathSum(root.right, targetSum-root.val))  