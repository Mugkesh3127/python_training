from collections import deque

# -----------------------------
# Tree Node
# -----------------------------
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# -----------------------------
# Zigzag Level Order Traversal
# -----------------------------
def zigzag_level_order(root):
    if root is None:
        return []

    result = []
    queue = deque([root])
    left_to_right = True

    while queue:
        level = []

        # Process all nodes in the current level
        for _ in range(len(queue)):
            node = queue.popleft()

            if left_to_right:
                level.append(node.val)
            else:
                level.insert(0, node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(level)

        # Toggle direction
        left_to_right = not left_to_right

    return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


# -----------------------------
# Test
# -----------------------------
print(zigzag_level_order(root))