# delete node in a bst
def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root: return
    else:
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                new_root = root.right
                root = None
                return new_root
            if not root.right:
                new_root = root.left
                root = None
                return new_root
            
            if root.left and root.right:
                current = root.right
                while current.left: current = current.left
                root.val = current.val
                root.right = self.deleteNode(root.right, root.val)
    return root