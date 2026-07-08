from collections import defaultdict

class GraphAdjList:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, directed=False):
        self.graph[u].append(v)

        if not directed:
            self.graph[v].append(u)

    def print_graph(self):
        print("Adjacency List:")
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")


# Example
g = GraphAdjList()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")

g.print_graph()


class GraphAdjMatrix:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matrix = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, directed=False):
        self.matrix[u][v] = 1

        if not directed:
            self.matrix[v][u] = 1

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.matrix:
            print(row)


# Example
g = GraphAdjMatrix(4)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)

g.print_graph()