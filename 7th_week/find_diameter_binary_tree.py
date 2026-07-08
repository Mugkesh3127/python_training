# -----------------------------
# Tree Node
# -----------------------------
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# -----------------------------
# Diameter of Binary Tree
# -----------------------------
def diameter_of_binary_tree(root):
    diameter = 0

    def height(node):
        nonlocal diameter

        if node is None:
            return 0

        # Height of left and right subtree
        left_height = height(node.left)
        right_height = height(node.right)

        # Update maximum diameter
        diameter = max(diameter, left_height + right_height)

        # Return height of current node
        return 1 + max(left_height, right_height)

    height(root)
    return diameter


root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Diameter:", diameter_of_binary_tree(root))