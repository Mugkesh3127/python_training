# -----------------------------
# Tree Node
# -----------------------------
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# -----------------------------
# Binary Search Tree
# -----------------------------
class BST:
    def __init__(self):
        self.root = None

    # -------------------------
    # Insert
    # -------------------------
    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if node is None:
            return TreeNode(val)

        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)

        return node

    # -------------------------
    # Search
    # -------------------------
    def search(self, val):
        return self._search(self.root, val)

    def _search(self, node, val):
        if node is None or node.val == val:
            return node

        if val < node.val:
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)

    # -------------------------
    # Delete
    # -------------------------
    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if node is None:
            return None

        # Search for the node
        if val < node.val:
            node.left = self._delete(node.left, val)

        elif val > node.val:
            node.right = self._delete(node.right, val)

        else:
            # -------- Case 1: Leaf Node --------
            if node.left is None and node.right is None:
                return None

            # -------- Case 2: One Child --------
            elif node.left is None:
                return node.right

            elif node.right is None:
                return node.left

            # -------- Case 3: Two Children --------
            # Find inorder successor (smallest in right subtree)
            successor = self._find_min(node.right)

            # Replace current node value
            node.val = successor.val

            # Delete successor
            node.right = self._delete(node.right, successor.val)

        return node

    # -------------------------
    # Find Minimum Node
    # -------------------------
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    # -------------------------
    # Inorder Traversal
    # -------------------------
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)


# -----------------------------
# Test
# -----------------------------
bst = BST()

values = [50, 30, 70, 20, 40, 60, 80]

for v in values:
    bst.insert(v)

print("Initial BST (Inorder):", bst.inorder())

# Search
print("Search 40:", "Found" if bst.search(40) else "Not Found")
print("Search 100:", "Found" if bst.search(100) else "Not Found")

# Delete Leaf Node
bst.delete(20)
print("\nAfter deleting leaf node (20):")
print(bst.inorder())

# Delete Node with One Child
bst.delete(30)
print("\nAfter deleting node with one child (30):")
print(bst.inorder())

# Delete Node with Two Children
bst.delete(70)
print("\nAfter deleting node with two children (70):")
print(bst.inorder())