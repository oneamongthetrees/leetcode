# search in a binary search tree
def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
# Misunderstood question...
# Thought it wanted entire subtree (lol)
'''
def search_subtree(root, val):
    subtree = []
    collect_subtree(root, val, subtree)
    return subtree
def collect_subtree(root, val, subtree):
    if root:
        current = root
        while current:
            if val < current.val:
                current = current.left
            elif val > current.val:
                current = current.right
            else:
                get_subtree(current, subtree)
                break
def get_subtree(root, subtree):
    subtree.append(root.val)
    if root.left:
        get_subtree(root.left, subtree)
    if root.right:
        get_subtree(root.right, subtree)
return search_subtree(root, val)
'''
if root:
    while root:
        if val < root.val: 
            root = root.left
        elif val > root.val:
            root = root.right
        else:
            return root
    
    return