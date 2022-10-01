# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # inorder traversal
        arr = self.traverse(root, [])
        
        # check if it is always increasing
        for i in range(len(arr)-1):
            if arr[i] >= arr[i+1]:
                return False
            
        return True
    
    def traverse(self, root, arr):
        
        if root is None:
            return arr
        
        else:
        
            arr = self.traverse(root.left, arr)
            arr += [root.val]
            return self.traverse(root.right, arr)
        
        
        
            
            