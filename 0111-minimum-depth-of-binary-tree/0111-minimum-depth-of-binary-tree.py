# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        # if left subtree does not exist
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        # if right subtree does not exist
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # if both children exist
        return 1 + min(self.minDepth(root.left),
                       self.minDepth(root.right))