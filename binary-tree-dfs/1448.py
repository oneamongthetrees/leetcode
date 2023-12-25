# count good nodes in binary tree
def goodNodes(self, root: TreeNode) -> int:
    good_nodes = 0
    def get_good_nodes(root, known_max=-999999):
		nonlocal good_nodes
        if not root: return 0
        else:
            if root.val >= known_max:
                good_nodes += 1
            known_max = max(known_max, root.val)
            get_good_nodes(root.left, known_max)
            get_good_nodes(root.right, known_max)
    get_good_nodes(root)
    return good_nodes