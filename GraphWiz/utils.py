# from graph import Graph
from graphElements import Vertex, Edge
from queue import SimpleQueue

class BFS:
    def __init__(self, graph) -> None:
        self.graph = graph
        self.index = 0
        self.level = {}
        self.predecessor = {}

    def execute(self, start_vertex:Vertex) -> tuple[dict, dict]:
        visited = set()
        queue = SimpleQueue()
        queue.put(start_vertex)
        self.level[start_vertex.label] = 0
        self.predecessor[start_vertex.label] = None

        while not queue.empty():
            current:Vertex = queue.get()
            if current.label not in visited:
                visited.add(current.label)

                for edge in self.graph.edges:
                    if edge.source.label == current.label:
                        neighbor = edge.target
                        if neighbor.label not in visited:
                            queue.put(neighbor)
                            self.level[neighbor.label] = self.level[current.label] + 1
                            self.predecessor[neighbor.label] = current.label

        return self.level, self.predecessor

class DFS:
    def __init__(self, graph) -> None:
        self.graph = graph
        self.time = 0
        self.discovery_time = {}
        self.finish_time = {}
        self.parent = {}

    def execute(self, start_vertex:Vertex) -> tuple[dict, dict, dict]:
        visited = set()
        self.parent[start_vertex.label] = None

        def dfs_recursive(vertex:Vertex) -> None:
            nonlocal visited

            visited.add(vertex.label)
            self.time += 1
            self.discovery_time[vertex.label] = self.time

            for edge in self.graph.edges:
                if edge.source.label == vertex.label:
                    neighbor = edge.target
                    if neighbor.label not in visited:
                        self.parent[neighbor.label] = vertex.label
                        dfs_recursive(neighbor)

            self.time += 1
            self.finish_time[vertex.label] = self.time

        dfs_recursive(start_vertex)
        return self.discovery_time, self.finish_time, self.parent