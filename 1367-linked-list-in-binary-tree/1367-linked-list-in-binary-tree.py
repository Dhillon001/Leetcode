class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        # Try to match starting at this root
        def match(list_node, tree_node):
            if not list_node:
                return True      # finished matching entire list
            if not tree_node:
                return False     # tree ended before list
            if list_node.val != tree_node.val:
                return False
            
            # try going left OR right
            return (match(list_node.next, tree_node.left) or
                    match(list_node.next, tree_node.right))
        
        
        if not root:
            return False
        
        # Either:
        # 1) match starting here
        # 2) or try left subtree
        # 3) or try right subtree
        return (match(head, root) or
                self.isSubPath(head, root.left) or
                self.isSubPath(head, root.right))