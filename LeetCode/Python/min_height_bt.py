# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def traverse(node, height, arr):
            
            if not (node.left or node.right):
                return arr + [height]
            else:
                
                if node.left:
                    arr = traverse(node.left, height + 1, arr)
                
                if node.right:
                    arr = traverse(node.right, height + 1, arr)
                    
                return arr

        if root is None:
            return 0
        else:
            return min(traverse(root, 1, []))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def height(node):
            if node is None:
                return 0
            else:
                left = height(node.left)
                right = height(node.right)
                         
                # do not include null trees (size 0)
                if left == 0:
                    return 1 + right
                elif right == 0:
                    return 1 + left
                else:
                    return 1 + min(left, right)
            
        return height(root)
            
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def traverse(node, height):
            
            if not(node.left or node.right):
                return height
            else:
                lh = float("inf")
                rh = float("inf")
                if node.left:
                    lh = traverse(node.left, height + 1)
                if node.right:
                    rh = traverse(node.right, height + 1)
                return min(lh,rh)
            
        if root is None:
            return 0
        else:
            return traverse(root, 1)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # predecessor map??
        
        if root is None:
            return 0
        
        q = [root]
        level = 1
        count = 0
        height = 1
        
        while q:
            
            if count == 2**level:
                height += 1
                level += 1
                count = 0
            
            curr = q.pop(0)
            
            if curr is None:
                q.append(None)
                q.append(None)
                count += 2
            elif not(curr.left or curr.right):
                return height
            else:
                q.append(curr.left)
                q.append(curr.right)
                count += 2

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # predecessor map??
        
        if root is None:
            return 0
        
        q = [root]
        height = 0
        
        while q:
            height += 1
            
            for _ in range(len(q)):
                curr = q.pop(0)
            
                if not(curr.left or curr.right):
                    return height
                else:
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)