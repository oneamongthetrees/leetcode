# maximum depth of binary tree    
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root: return 0
    else:
        left = right = 0
        if root.left:
            left = self.maxDepth(root.left)
        if root.right:
            right = self.maxDepth(root.right)
        return 1 + max(left, right) 