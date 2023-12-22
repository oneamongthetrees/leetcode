# leaf-similar trees
def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def get_leaves(root):
        leaves = []
        collect_leaves(root, leaves)
        print(leaves)
        return leaves
    def collect_leaves(root, leaves):
        if root:
            if not root.left and not root.right:
                leaves.append(root.val)
            else:
                if root.left:
                    collect_leaves(root.left, leaves)
                if root.right:
                    collect_leaves(root.right, leaves)
    return get_leaves(root1) == get_leaves(root2)