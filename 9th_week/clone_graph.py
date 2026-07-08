class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(node):
    if not node:
        return None

    # Original node -> Cloned node
    visited = {}

    def dfs(curr):
        # Return cloned node if already created
        if curr in visited:
            return visited[curr]

        # Create clone
        clone = Node(curr.val)
        visited[curr] = clone

        # Clone neighbors
        for neighbor in curr.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)