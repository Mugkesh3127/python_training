# -----------------------------
# Tree Node
# -----------------------------
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# -----------------------------
# Build Tree from Preorder & Inorder
# -----------------------------
def build_tree(preorder, inorder):

    # Store inorder indices for O(1) lookup
    inorder_index = {value: i for i, value in enumerate(inorder)}

    preorder_index = 0

    def helper(left, right):
        nonlocal preorder_index

        # No nodes in this subtree
        if left > right:
            return None

        # Root is the current preorder element
        root_value = preorder[preorder_index]
        preorder_index += 1

        root = TreeNode(root_value)

        # Find root position in inorder
        mid = inorder_index[root_value]

        # Build left subtree
        root.left = helper(left, mid - 1)

        # Build right subtree
        root.right = helper(mid + 1, right)

        return root

    return helper(0, len(inorder) - 1)


# -----------------------------
# Inorder Traversal (Verification)
# -----------------------------
def inorder_traversal(root):
    if root is None:
        return []

    return (
        inorder_traversal(root.left)
        + [root.val]
        + inorder_traversal(root.right)
    )


# -----------------------------
# Preorder Traversal (Verification)
# -----------------------------
def preorder_traversal(root):
    if root is None:
        return []

    return (
        [root.val]
        + preorder_traversal(root.left)
        + preorder_traversal(root.right)
    )


# -----------------------------
# Example
# -----------------------------
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

root = build_tree(preorder, inorder)

print("Preorder:", preorder_traversal(root))
print("Inorder :", inorder_traversal(root))