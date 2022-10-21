# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # find the max height on left side and right side, check if >1 difference
        # go until it is a left node
        # find subheight of both sides, and take the max out of them
        
        def get_height_count(node):
            
            if node is None:
                return 0, 0
            
            lh, rh = 0, 0
            if node.left:
                lh = 1
                lh += max(get_height_count(node.left))
            if node.right:
                rh = 1
                rh += max(get_height_count(node.right))
                
            return lh, rh
                
        # tree traversal (pre order)
        
        if root is not None:
            
            if root.left:
                if not self.isBalanced(root.left):
                    return False
                
            if root.right:
                if not self.isBalanced(root.right):
                    return False
            
            lh, rh = get_height_count(root)
            return abs(lh - rh) <= 1
        
        else:
            
            return True
            
            
            
            
        
    
    # traverse array, and see if the split is close
    
    # get height count of each node encountered and check if the abs condition satisfy