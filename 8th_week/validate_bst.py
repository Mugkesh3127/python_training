# -----------------------------
# Tree Node
# -----------------------------
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# -----------------------------
# Validate BST
# -----------------------------
def is_valid_bst(root):

    def validate(node, low, high):
        if node is None:
            return True

        # Current node must be within (low, high)
        if node.val <= low or node.val >= high:
            return False

        # Left subtree: values < node.val
        # Right subtree: values > node.val
        return (
            validate(node.left, low, node.val) and
            validate(node.right, node.val, high)
        )

    return validate(root, float("-inf"), float("inf"))

root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.right = TreeNode(7)

root1.left.left = TreeNode(2)
root1.left.right = TreeNode(4)

root1.right.left = TreeNode(6)
root1.right.right = TreeNode(8)

print(is_valid_bst(root1))   # True

root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(7)
root2.right.left = TreeNode(4)

print(is_valid_bst(root2))   # False