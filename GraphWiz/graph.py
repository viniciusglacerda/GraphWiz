import re
from GraphWiz.graphElements import Vertex, Edge
from GraphWiz.utils import BFS, DFS, BridgeFinder, FleuryAlgorithm, print_progress_bar

class Graph:
    def __init__(self, qtd_vertices:int=0, is_directed:bool=False, vertices_labels:list[str]=[]) -> None:
        # Deve ser implementado a criação de um grafo com X vértices (o número de vértices deve ser inserido pelo usuário)
        self.qtd_vertices = qtd_vertices
        self.is_directed = is_directed
        self.vertex_dict:dict[int, Vertex] = {}
        for index in range(qtd_vertices):
            v = Vertex()
            try: v.label = vertices_labels[index]
            except IndexError: v.label = index+1
            self.vertex_dict.update({index: v})
            print_progress_bar(index+1, qtd_vertices, prefix='Graph Creation Progress:', suffix='Complete', length=50)
            
        self.edges_list:list[Edge] = []
    
    @property
    def vertices(self):
        return self.vertex_dict
    
    @vertices.setter
    def vertices(self, vertices):
        self.vertex_dict = vertices
    
    @property
    def edges(self):
        return self.edges_list
    
    @edges.setter
    def edges(self, edges):
        self.edges_list = edges

    def corresponding_edge(self, src_label:str|int, target_label:str|int) -> Edge | None:
        for edge in self.edges_list:
            src_vertex:Vertex = edge.source
            target_vertex:Vertex = edge.target
            if  src_vertex.label == src_label and target_vertex.label == target_label:
                return edge
        return None
    
    def vertex_by_label(self, label:str|int) -> Vertex | None:
        for vertex in self.vertex_dict.values():
            if vertex.label == label:
                return vertex
        return None
            
    def show_matrix(self) -> None:
        print("    ", end="")
        [print(f"{self.vertex_dict.get(key).label}", end="  ") for key in self.vertex_dict]
        print("\n")
        for key in self.vertex_dict:
            print(f"{self.vertex_dict.get(key).label}  ", end="|")
            for key_j in self.vertex_dict:
                edge = self.corresponding_edge(self.vertex_dict.get(key).label, self.vertex_dict.get(key_j).label)
                if edge:
                    print(f"{edge.weight}", end="|")
                else:
                    print(f"", end=" |")
            print("")

    def show_list(self) -> None:
        for vertex in self.vertex_dict.values():
            print(f"[{vertex.label}] ->", end=" ")
            for edge in self.edges_list:
                v1, v2 = edge.source, edge.target
                if v1.label == vertex.label:
                    print(f"[{v2.label}] ->", end=" ")
            print("")
    
    def add_new_vertices(self, qtd:int=1, labels:list[str|int]=[]) -> None:
        count = len(self.vertex_dict)
        for i in range(len(self.vertex_dict), len(self.vertex_dict)+qtd):
            v = Vertex()
            try: v.label = labels[i - count]
            except IndexError: v.label = i+1
            self.vertex_dict[i] = v

    def remove_vertice(self, vertex_label:str|int) -> None:
        to_remove = []
        for key in self.vertex_dict:
            if self.vertex_dict.get(key).label == vertex_label:
                to_remove.append(key)
                
        self.vertex_dict = {key: value for key, value in self.vertex_dict.items() if key not in to_remove and not None}

    def create_edge(self, src_label:str|int, target_label:str|int) -> None:
        # Deve ser implementado criação de arestas
        edge = Edge()
        edge.source = self.vertex_by_label(src_label)
        edge.target = self.vertex_by_label(target_label)

        if edge.source is None or edge.target is None:
            raise ValueError

        if not self.is_directed:
            edge2 = Edge()
            edge2.source = edge.target
            edge2.target = edge.source
            self.edges_list.append(edge2)

        self.edges_list.append(edge)

    def remove_edge(self, src_label:str|int, target_label:str|int) -> None:
        # Remoção de arestas
        edge = self.corresponding_edge(src_label, target_label)
        if edge: self.edges_list.remove(edge)
        if not self.is_directed:
            edge = self.corresponding_edge(target_label, src_label)
            if edge: self.edges_list.remove(edge)
    
    def vertex_weighting(self, vertex_label:str|int, weight:int) -> None:
        # Ponderação de vértices
        vertex = self.vertex_by_label(vertex_label)
        if vertex: vertex.weight = weight
        else: raise ValueError

    def vertex_labeling(self, vertex_label:str|int, new_label:str) -> None:
        # Rotulação de vértices
        vertex = self.vertex_by_label(vertex_label)
        if vertex: vertex.label = new_label
        else: raise ValueError
    
    def edge_weighting(self, src_label:str|int, target_label:str|int, weight:int=1) -> None:
        # Ponderação de arestas
        edge = self.corresponding_edge(src_label, target_label)
        if edge: edge.weight = weight
        else: raise ValueError
        
        if not self.is_directed: 
            edge = self.corresponding_edge(target_label, src_label)
            if edge: edge.weight = weight

    def edge_labeling(self, src_label:str|int, target_label:str|int, label:str) -> None:
        # Rotulação de arestas
        edge = self.corresponding_edge(src_label, target_label)
        if edge: edge.label = label
        else: raise ValueError
        
        if not self.is_directed: 
            edge = self.corresponding_edge(target_label, src_label)
            if edge: edge.label = label

    def vertex_adjacency_check(self, src_label:str|int, target_label:str|int) -> bool:
        # Checagem de adjacencia entre vertices
        return True if self.corresponding_edge(src_label, target_label) else False
    
    def edge_adjacency_check(self, edge1: Edge, edge2: Edge) -> bool:
        # Checagem de adjacencia entre arestas
        return edge1.target == edge2.source or edge1.source == edge2.target
    
    def exist_edge(self, src_label:str|int, target_label:str|int) -> bool:
        # Verifica existência de aresta
        return True if self.corresponding_edge(src_label, target_label) else False

    def count_edge(self) -> int:
        # Checa a quantidade de arestas
        length = len(self.edges_list)
        return int(length / 2) if not self.is_directed and length > 0 else length

    def count_vertex(self) -> int:
        # Checa a quantidade de vértices
        return len(self.vertex_dict)

    def is_empty(self) -> bool:
        # Checa se o grafo é vazio: um grafo vazio é um grafo com vertices mas sem arestas
        return False if self.vertex_dict and self.edges_list else True

    def is_complete(self) -> bool:
        # Checa se o grafo é completo
        edge_quantity = len(self.vertex_dict) * (len(self.vertex_dict)-1) / 2
        return True if self.count_edge() == edge_quantity else False

    def get_vertex_degree(self, vertex_label: str|int) -> int:
        if vertex_label in self.vertices:
            degree = 0
            for edge in self.edges_list:
                if edge.source.label == vertex_label or edge.target.label == vertex_label:
                    degree += 1
            return degree
        else:
            return 0

    def bfs(self, start_vertex:Vertex=None) -> tuple[dict]:
        if start_vertex is None:
            start_vertex = next(iter(self.vertices.values()), None)

        if start_vertex is not None:
            bfs_instance = BFS(self)
            return bfs_instance.execute(start_vertex)
        else:
            return {}, {}
    
    def dfs(self, start_vertex:Vertex=None) -> tuple[dict]:
        if start_vertex is None:
            start_vertex = next(iter(self.vertices.values()), None)

        if start_vertex is not None:
            dfs_instance = DFS(self)
            return dfs_instance.execute(start_vertex)
        else:
            return {}, {}, {}
    
    def bridge_naive_method(self) -> list[Edge]:
        bf = BridgeFinder(self)
        return bf.naive_bridges()

    def bridge_tarjan_method(self) -> list[Edge]:
        bf = BridgeFinder(self)
        return bf.tarjan_bridges()

    def eulerian_path(self, method:str="naive"):
        fleury_algorithm = FleuryAlgorithm()

        eulerian_path = fleury_algorithm.find_eulerian_path(self, method)
        print("Eulerian Path:")
        print(" -> ".join(eulerian_path))
    
    def to_gexf(self, file_path:str="", file_name:str="graph.gexf") -> None:
        with open(file_path+file_name, 'w') as file:
            file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            file.write('<gexf xmlns="http://www.gexf.net/1.2draft" version="1.2">\n')
            file.write('\t<graph mode="static" defaultedgetype="undirected">\n')

            # Escreve os vértices
            file.write('\t\t<nodes>\n')
            for vertex_label, vertex in self.vertices.items():
                file.write(f'\t\t\t<node id="{vertex_label}" label="{vertex.label}" />\n')
            file.write('\t\t</nodes>\n')

            # Escreve as arestas
            file.write('\t\t<edges>\n')
            for edge in self.edges_list:
                file.write(f'\t\t\t<edge source="{edge.source.label}" target="{edge.target.label}" />\n')
            file.write('\t\t</edges>\n')

            file.write('\t</graph>\n')
            file.write('</gexf>\n')

    def from_gexf(self, file_path: str="") -> None:
        # Limpa o grafo atual antes de carregar um novo
        self.vertices.clear()
        self.edges_list.clear()

        with open(file_path, 'r') as file:
            in_nodes_section = False
            in_edges_section = False

            for line in file:
                line = line.strip()

                if line == '<nodes>':
                    in_nodes_section = True
                    in_edges_section = False
                elif line == '<edges>':
                    in_nodes_section = False
                    in_edges_section = True
                elif line in ('</nodes>', '</edges>'):
                    in_nodes_section = False
                    in_edges_section = False
                elif in_nodes_section and line.startswith('<node '):
                    match = re.search(r'label="([^"]+)"', line)
                    if match:
                        vertex_label = match.group(1)
                        self.add_new_vertices(qtd=1, labels=[vertex_label])
                elif in_edges_section and line.startswith('<edge '):
                    source_match = re.search(r'source="([^"]+)"', line)
                    target_match = re.search(r'target="([^"]+)"', line)

                    if source_match and target_match:
                        source_label = source_match.group(1)
                        target_label = target_match.group(1)
                        self.create_edge(str(source_label), str(target_label))