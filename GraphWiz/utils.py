# from graph import Graph
from GraphWiz.graphElements import Vertex, Edge
from queue import SimpleQueue
from copy import deepcopy

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

    def execute(self, start_vertex: Vertex) -> tuple[dict, dict, dict]:
        visited = set()
        self.parent[start_vertex.label] = None

        def dfs_recursive(vertex: Vertex) -> None:
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

        # Verifica se o vértice inicial existe no grafo antes de iniciar a DFS
        vertex_labels = [lbl.label for lbl in list(self.graph.vertices.values())]
        if start_vertex.label in vertex_labels:
            dfs_recursive(start_vertex)

        return self.discovery_time, self.finish_time, self.parent

class BridgeFinder:
    def __init__(self, graph) -> None:
        self.graph = graph
        self.original_level, _ = graph.bfs()
    
    def is_bridge_naive(self, src_label: str | int, target_label: str | int) -> bool:
        # Método "naive" para testar pontes usando BFS

        temp_graph = deepcopy(self.graph)

        temp_graph.remove_edge(src_label, target_label)

        level, _ = temp_graph.bfs()

        return len(level) != len(self.original_level)
    
    def naive_bridges(self) -> list:
        bridges = []
        for edge in self.graph.edges:
            if self.is_bridge_naive(edge.source.label, edge.target.label):
                if edge.label:
                    bridges.append(edge.label)
                else:
                    bridges.append((edge.source.label, edge.target.label))
        return bridges

    def tarjan_bridges(self) -> list[tuple[str | int, str | int]]:
        visited = set()
        result = []
        discovery_time, finish_time, parent = self.graph.dfs()

        def tarjan_recursive(vertex: Vertex, time: int) -> list[tuple[str | int, str | int]]:
            nonlocal visited
            nonlocal result

            visited.add(vertex.label)
            discovery_time[vertex.label] = time
            low_time = time

            for edge in self.graph.edges_list:
                if edge.source.label == vertex.label:
                    neighbor = edge.target
                    if neighbor.label not in visited:
                        low_time_neighbor = tarjan_recursive(neighbor, time + 1)

                        low_time = min(low_time, low_time_neighbor)

                        if low_time_neighbor > discovery_time[vertex.label]:
                            result.append((vertex.label, neighbor.label))

                    elif neighbor.label != parent[vertex.label]:
                        low_time = min(low_time, discovery_time[neighbor.label])

            return low_time

        for vertex in self.graph.vertices.values():
            if vertex.label not in visited:
                tarjan_recursive(vertex, 0)

        return result

class FleuryAlgorithm:
    @staticmethod
    def is_eulerian(graph) -> bool:
        if not graph.vertices:
            return False

        odd_degree_count = 0
        for vertex in graph.vertices.values():
            degree = graph.get_vertex_degree(vertex.label)
            if degree % 2 != 0:
                odd_degree_count += 1

        return odd_degree_count == 0 or odd_degree_count == 2

    @staticmethod
    def find_eulerian_path(graph, method:str="naive") -> list[str]:
        if not FleuryAlgorithm.is_eulerian(graph):
            print("O grafo não é euleriano.")
            return []

        bridges_list = graph.bridge_tarjan_method() if method == "tarjan" else graph.bridge_naive_method()
        temp_edges = graph.edges_list.copy()

        def is_valid_edge(edge):
            # Verifica se a aresta é uma ponte
            return edge.label not in bridges_list

        def dfs(current_vertex):
            path = []
            for edge in temp_edges:
                if edge.source.label == current_vertex.label and is_valid_edge(edge):
                    temp_edges.remove(edge)
                    path += dfs(edge.target)
                    path.append(f"({current_vertex.label} -> {edge.target.label})")

            return path

        start_vertex = next(iter(graph.vertices.values()))
        return dfs(start_vertex)