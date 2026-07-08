class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Maximum Depth
# -----------------------------
def max_depth(root):
    if root is None:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))


# Minimum Depth
# -----------------------------
def min_depth(root):
    if root is None:
        return 0

    # Leaf node
    if root.left is None and root.right is None:
        return 1

    # Only right subtree exists
    if root.left is None:
        return 1 + min_depth(root.right)

    # Only left subtree exists
    if root.right is None:
        return 1 + min_depth(root.left)

    # Both children exist
    return 1 + min(min_depth(root.left), min_depth(root.right))

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.right = TreeNode(6)

root.left.left.left = TreeNode(7)


# Test
# -----------------------------
print("Maximum Depth:", max_depth(root))
print("Minimum Depth:", min_depth(root))