# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def recursive_call(subnums):
            
            if not subnums:
                return None
            elif len(subnums) == 1:
                return TreeNode(subnums[0])
            else:
                mid_index = len(subnums) // 2
                root = TreeNode(subnums[mid_index])

                root.left = recursive_call(subnums[:mid_index])
                root.right = recursive_call(subnums[mid_index+1:])

                return root
        
        return recursive_call(nums)
        
            