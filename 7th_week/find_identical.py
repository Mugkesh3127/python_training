# -----------------------------
# Tree Node
# -----------------------------
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# -----------------------------
# Check if two trees are identical
# -----------------------------
def is_identical(root1, root2):
    # Both trees are empty
    if root1 is None and root2 is None:
        return True

    # One tree is empty
    if root1 is None or root2 is None:
        return False

    # Compare current node and subtrees
    return (
        root1.val == root2.val
        and is_identical(root1.left, root2.left)
        and is_identical(root1.right, root2.right)
    )


# -----------------------------
# Check if subRoot is a subtree of root
# -----------------------------
def is_subtree(root, subRoot):
    # Empty subtree is always a subtree
    if subRoot is None:
        return True

    # Main tree exhausted
    if root is None:
        return False

    # Trees match from this node
    if is_identical(root, subRoot):
        return True

    # Search left and right subtrees
    return (
        is_subtree(root.left, subRoot) or
        is_subtree(root.right, subRoot)
    )


root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

another = TreeNode(4)
another.left = TreeNode(1)
another.right = TreeNode(3)


# -----------------------------
# Test
# -----------------------------
print("Identical (subRoot vs another):", is_identical(subRoot, another))
print("Identical (subRoot vs subRoot):", is_identical(subRoot, subRoot))
print("Is subRoot a subtree of root?:", is_subtree(root, subRoot))
print("Is another a subtree of root?:", is_subtree(root, another))