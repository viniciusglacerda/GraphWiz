# from graph import Graph
from multiprocessing import Pool
from GraphWiz.graphElements import Vertex, Edge
from queue import SimpleQueue

def print_progress_bar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    # Print newline on completion
    if iteration == total:
        print()

class BFS:
    def __init__(self, graph) -> None:
        self.graph = graph
        self.index = 0
        self.level = {}
        self.predecessor = {}

    def execute(self, start_vertex: Vertex) -> tuple[dict, dict]:
        visited = set()
        queue = SimpleQueue()
        queue.put(start_vertex)
        self.level[start_vertex.label] = 0
        self.predecessor[start_vertex.label] = None

        # Usando um dicionário para armazenar as adjacências
        adjacency_dict = {vertex.label: [edge.target for edge in self.graph.edges if edge.source.label == vertex.label] for vertex in self.graph.vertices.values()}
        vertices = {vertex.label: vertex for vertex in self.graph.vertices.values()}

        while not queue.empty():
            current: Vertex = queue.get()
            if current.label not in visited:
                visited.add(current.label)

                for neighbor_label in adjacency_dict[current.label]:
                    if neighbor_label not in visited:
                        neighbor = vertices[neighbor_label.label]
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
        original_edge_count = len(self.graph.edges)
        self.graph.remove_edge(src_label, target_label)
        modified_edge_count = len(self.graph.edges)
        return original_edge_count != modified_edge_count

    def _process_edge(self, args):
        edge, i, tot_v = args
        result = None
        if self.is_bridge_naive(edge.source.label, edge.target.label):
            if edge.label:
                result = edge.label
            else:
                result = (edge.source.label, edge.target.label)
        print_progress_bar(i, tot_v, prefix='Naive Bridges Progress:', suffix='Complete', length=50)
        return result

    def naive_bridges(self) -> list:
        with Pool() as pool:
            args_list = [(edge, i, len(self.graph.edges)) for i, edge in enumerate(self.graph.edges)]
            results = list(filter(None, pool.map(self._process_edge, args_list)))
        return results

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

        for i, vertex in enumerate(graph.vertices.values()):
            odd_degree_count += 1 if graph.get_vertex_degree(vertex.label) % 2 != 0 else 0
            print_progress_bar(i + 1, len(graph.vertices), prefix='Verifying Eulerian Properties:', suffix='Complete', length=50)

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

        def dfs_iterative(start_vertex):
            stack = [start_vertex]
            path = []
            visited = set()

            i=1
            tot_v = len(graph.vertices)
            while stack:
                current_vertex = stack.pop()
                if current_vertex.label not in visited:
                    visited.add(current_vertex.label)
                    path.append(str(current_vertex.label))

                    for edge in temp_edges:
                        if edge.source.label == current_vertex.label and is_valid_edge(edge):
                            stack.append(edge.target)
                    print_progress_bar(i, tot_v, prefix='DFS Progress:', suffix='Complete', length=50)
                    i+=1

            return path

        start_vertex = next(iter(graph.vertices.values()))
        return dfs_iterative(start_vertex)