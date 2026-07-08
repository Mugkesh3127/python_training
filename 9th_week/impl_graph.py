from collections import defaultdict, deque


class Graph:
    def __init__(self):
        # Adjacency list
        self.adj = defaultdict(list)

    def add_edge(self, u, v, directed=False):
        """
        Add an edge to the graph.

        Parameters:
        u : Source vertex
        v : Destination vertex
        directed : If True, creates a directed edge.
                   If False, creates an undirected edge.
        """
        self.adj[u].append(v)

        if not directed:
            self.adj[v].append(u)

    def bfs(self, start):
        """
        Breadth-First Search (BFS)

        Returns:
            List of nodes in BFS traversal order.
        """
        visited = set()
        queue = deque()
        result = []

        visited.add(start)
        queue.append(start)

        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    def dfs(self, start, visited=None):
        """
        Depth-First Search (DFS) using recursion.

        Returns:
            List of nodes in DFS traversal order.
        """
        if visited is None:
            visited = set()

        visited.add(start)
        result = [start]

        for neighbor in self.adj[start]:
            if neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))

        return result


# ---------------- Example Usage ----------------

g = Graph()

# Undirected graph
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')

print("Adjacency List:")
for node in g.adj:
    print(node, "->", g.adj[node])

print("\nBFS Traversal:")
print(g.bfs('A'))

print("\nDFS Traversal:")
print(g.dfs('A'))


# ---------------- Directed Graph Example ----------------

dg = Graph()

dg.add_edge(1, 2, directed=True)
dg.add_edge(1, 3, directed=True)
dg.add_edge(2, 4, directed=True)
dg.add_edge(3, 5, directed=True)

print("\nDirected Graph Adjacency List:")
for node in dg.adj:
    print(node, "->", dg.adj[node])

print("\nBFS Traversal (Directed):")
print(dg.bfs(1))

print("\nDFS Traversal (Directed):")
print(dg.dfs(1))