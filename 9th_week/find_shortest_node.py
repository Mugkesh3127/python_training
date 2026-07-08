from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, directed=False):
        self.graph[u].append(v)

        if not directed:
            self.graph[v].append(u)

    def shortest_path(self, start, end):
        # If start and end are the same
        if start == end:
            return [start]

        visited = set([start])
        queue = deque([start])
        parent = {start: None}

        while queue:
            node = queue.popleft()

            # Destination found
            if node == end:
                break

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    queue.append(neighbor)

        # No path exists
        if end not in parent:
            return []

        # Reconstruct path
        path = []
        curr = end

        while curr is not None:
            path.append(curr)
            curr = parent[curr]

        return path[::-1]   # Reverse the path


# Example
g = Graph()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")
g.add_edge("D", "F")
g.add_edge("E", "F")

print("Shortest Path:", g.shortest_path("A", "F"))