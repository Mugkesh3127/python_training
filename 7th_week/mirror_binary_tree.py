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
# Build Tree from Level Order List
# -----------------------------
def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values):
            node.left = TreeNode(values[i])
            queue.append(node.left)
            i += 1

        if i < len(values):
            node.right = TreeNode(values[i])
            queue.append(node.right)
            i += 1

    return root


# -----------------------------
# Invert Binary Tree
# -----------------------------
def invert_tree(root):
    if root is None:
        return None

    # Swap left and right
    root.left, root.right = root.right, root.left

    # Recursively invert subtrees
    invert_tree(root.left)
    invert_tree(root.right)

    return root


# -----------------------------
# Level Order Traversal
# -----------------------------
def level_order(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        level = []

        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


# -----------------------------
# Test
# -----------------------------
values = [4, 2, 7, 1, 3, 6, 9]

root = build_tree(values)

print("Before Inversion:")
print(level_order(root))

invert_tree(root)

print("After Inversion:")
print(level_order(root))