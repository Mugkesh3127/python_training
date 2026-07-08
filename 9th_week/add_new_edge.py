from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def will_create_cycle(self, u, v):
        # Temporarily add the new edge
        self.graph[u].append(v)

        state = {}  # 0 = Unvisited, 1 = Visiting, 2 = Visited

        def dfs(node):
            if state.get(node, 0) == 1:
                return True      # Cycle found

            if state.get(node, 0) == 2:
                return False     # Already processed

            state[node] = 1      # Mark as Visiting

            for neighbor in self.graph[node]:
                if dfs(neighbor):
                    return True

            state[node] = 2      # Mark as Visited
            return False

        # Check all nodes
        has_cycle = False
        for node in list(self.graph.keys()):
            if state.get(node, 0) == 0:
                if dfs(node):
                    has_cycle = True
                    break

        # Remove the temporary edge
        self.graph[u].pop()

        return has_cycle


# Example
g = Graph()

g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)

print("Adding edge 3 -> 1 creates cycle:",
      g.will_create_cycle(3, 1))

print("Adding edge 3 -> 4 creates cycle:",
      g.will_create_cycle(3, 4))