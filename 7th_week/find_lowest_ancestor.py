# -----------------------------
# Tree Node
# -----------------------------
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# -----------------------------
# Lowest Common Ancestor
# (Binary Tree)
# -----------------------------
def lowest_common_ancestor(root, p, q):
    if root is None:
        return None

    if root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    # p and q are found in different subtrees
    if left and right:
        return root

    # Return whichever side is non-empty
    return left if left else right


root = TreeNode(3)

root.left = TreeNode(5)
root.right = TreeNode(1)

root.left.left = TreeNode(6)
root.left.right = TreeNode(2)

root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

p = root.left              # Node 5
q = root.left.right.right  # Node 4

lca = lowest_common_ancestor(root, p, q)

print("Lowest Common Ancestor:", lca.val)