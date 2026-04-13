# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # both nodes are None → same
        if not p and not q:
            return True
        
        # one is None OR values differ → not same
        if not p or not q or p.val != q.val:
            return False
        
        # recursively check left and right
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)