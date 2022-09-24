# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    
    levels = []
    
    q = [root]
    
    current_level = 0
    num_nodes = 0
    while len(q) != 0:
        node = q.pop(0)
            
        if node != None:
            
            # need to create the index before accessing it
            if len(levels) == current_level:
                levels.append([])
            # add the value to the current array
            levels[current_level] += [node.val]
            
        num_nodes += 1 # add to num_nodes even if node is None to maintain the levels
        
        if num_nodes >= current_level * 2:
            current_level += 1
            num_nodes = 0 # reset the number of nodes
            
        if node != None:
            q.append(node.left)
            q.append(node.right)
        
    return levels

def main():

    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    levels = levelOrder(root)
    print(levels)

main()
            
