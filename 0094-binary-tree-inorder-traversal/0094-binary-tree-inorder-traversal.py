# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional, List

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)      # Left
            result.append(node.val)  # Node
            dfs(node.right)     # Right
        
        dfs(root)
        return result