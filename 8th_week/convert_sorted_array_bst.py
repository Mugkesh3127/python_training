# -----------------------------
# Tree Node
# -----------------------------
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# -----------------------------
# Sorted Array -> Balanced BST
# -----------------------------
def sorted_array_to_bst(nums):

    def build(left, right):
        if left > right:
            return None

        # Choose middle element as root
        mid = (left + right) // 2

        root = TreeNode(nums[mid])

        # Build left and right subtrees
        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)

        return root

    return build(0, len(nums) - 1)


# -----------------------------
# Inorder Traversal (Verification)
# -----------------------------
def inorder(root):
    if root is None:
        return []

    return inorder(root.left) + [root.val] + inorder(root.right)


# -----------------------------
# Test
# -----------------------------
nums = [-10, -3, 0, 5, 9]

root = sorted_array_to_bst(nums)

print("Inorder Traversal:", inorder(root))