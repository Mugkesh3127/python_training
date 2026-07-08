from collections import deque


# Tree Node
# -----------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive Traversals
# =====================================================

def preorder_recursive(root):
    if root is None:
        return []
    return [root.val] + preorder_recursive(root.left) + preorder_recursive(root.right)


def inorder_recursive(root):
    if root is None:
        return []
    return inorder_recursive(root.left) + [root.val] + inorder_recursive(root.right)


def postorder_recursive(root):
    if root is None:
        return []
    return postorder_recursive(root.left) + postorder_recursive(root.right) + [root.val]


def level_order_recursive(root):
    result = []

    def helper(node, level):
        if node is None:
            return

        if len(result) == level:
            result.append([])

        result[level].append(node.val)

        helper(node.left, level + 1)
        helper(node.right, level + 1)

    helper(root, 0)
    return result


# Iterative Traversals
# =====================================================

def preorder_iterative(root):
    if root is None:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


def inorder_iterative(root):
    stack = []
    result = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result


def postorder_iterative(root):
    if root is None:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return result[::-1]


def level_order_iterative(root):
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


root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(11)

root.right.left.left = TreeNode(12)
root.right.left.right = TreeNode(13)
root.right.right.left = TreeNode(14)
root.right.right.right = TreeNode(15)


# Test All Traversals
# =====================================================

print("========== Recursive ==========")
print("Preorder :", preorder_recursive(root))
print("Inorder  :", inorder_recursive(root))
print("Postorder:", postorder_recursive(root))
print("LevelOrder:")
print(level_order_recursive(root))

print("\n========== Iterative ==========")
print("Preorder :", preorder_iterative(root))
print("Inorder  :", inorder_iterative(root))
print("Postorder:", postorder_iterative(root))
print("LevelOrder:")
print(level_order_iterative(root))