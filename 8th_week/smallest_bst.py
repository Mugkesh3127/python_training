# -----------------------------
# Tree Node
# -----------------------------
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# -----------------------------
# Kth Smallest Element
# -----------------------------
def kth_smallest(root, k):
    stack = []
    current = root
    count = 0

    while stack or current:

        # Go to the leftmost node
        while current:
            stack.append(current)
            current = current.left

        # Visit node
        current = stack.pop()
        count += 1

        # kth smallest found
        if count == k:
            return current.val

        # Move to right subtree
        current = current.right

    return None


root = TreeNode(5)

root.left = TreeNode(3)
root.right = TreeNode(6)

root.left.left = TreeNode(2)
root.left.right = TreeNode(4)

root.left.left.left = TreeNode(1)

k = 3

print(f"{k}rd Smallest:", kth_smallest(root, k))