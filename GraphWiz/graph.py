from graphElements import Vertex, Edge

class Graph:
    def __init__(self, qtd_vertices:int=0, is_directed:bool=False, vertices_labels:list[str]=[]) -> None:
        # Deve ser implementado a criação de um grafo com X vértices (o número de vértices deve ser inserido pelo usuário)
        self.qtd_vertices = qtd_vertices
        self.is_directed = is_directed
        self.vertices:dict[int, Vertex] = {}
        for index in range(qtd_vertices):
            v = Vertex()
            try: v.label = vertices_labels[index]
            except IndexError: v.label = index+1
            self.vertices.update({index: v})
            
        self.edges:list[Edge] = []

    def corresponding_edge(self, src_label:str|int, target_label:str|int) -> Edge | None:
        for edge in self.edges:
            src_vertex:Vertex = edge.source
            target_vertex:Vertex = edge.target
            if  src_vertex.label == src_label and target_vertex.label == target_label:
                return edge
        return None
    
    def vertex_by_label(self, label:str|int) -> Vertex | None:
        for vertex in self.vertices.values():
            if vertex.label == label:
                return vertex
        return None
            
    def show_matrix(self) -> None:
        print("    ", end="")
        [print(f"{self.vertices.get(key).label}", end="  ") for key in self.vertices]
        print("\n")
        for key in self.vertices:
            print(f"{self.vertices.get(key).label}  ", end="|")
            for key_j in self.vertices:
                edge = self.corresponding_edge(self.vertices.get(key).label, self.vertices.get(key_j).label)
                if edge:
                    print(f"{edge.weight}", end="|")
                else:
                    print(f"", end=" |")
            print("")

    def show_list(self) -> None:
        for vertex in self.vertices.values():
            print(f"[{vertex.label}] ->", end=" ")
            for edge in self.edges:
                v1, v2 = edge.source, edge.target
                if v1.label == vertex.label:
                    print(f"[{v2.label}] ->", end=" ")
            print("")
    
    def add_new_vertices(self, qtd:int=1, labels:list[str|int]=[]) -> None:
        count = len(self.vertices)
        for i in range(len(self.vertices), len(self.vertices)+qtd):
            v = Vertex()
            try: v.label = labels[i - count]
            except IndexError: v.label = i+1
            self.vertices[i] = v

    def remove_vertice(self, vertex_label:str|int) -> None:
        to_remove = []
        for key in self.vertices:
            if self.vertices.get(key).label == vertex_label:
                to_remove.append(key)
                
        self.vertices = {key: value for key, value in self.vertices.items() if key not in to_remove and not None}

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
            self.edges.append(edge2)

        self.edges.append(edge)

    def remove_edge(self, src_label:str|int, target_label:str|int) -> None:
        # Remoção de arestas
        self.edges.remove(self.corresponding_edge(src_label, target_label))
        if not self.is_directed:
            self.edges.remove(self.corresponding_edge(target_label, src_label))
    
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
    
    def edge_adjacency_check(self):
        # Checagem de adjacencia entre arestas
        ...
    
    def exist_edge(self, src_label:str|int, target_label:str|int) -> bool:
        # Verifica existência de aresta
        return True if self.corresponding_edge(src_label, target_label) else False

    def count_edge(self) -> int:
        # Checa a quantidade de arestas
        length = len(self.edges)
        return int(length / 2) if not self.is_directed and length > 0 else length

    def count_vertex(self) -> int:
        # Checa a quantidade de vértices
        return len(self.vertices)

    def is_empty(self) -> bool:
        # Checa se o grafo é vazio: um grafo vazio é um grafo com vertices mas sem arestas
        return False if self.vertices and self.edges else True

    def is_complete(self) -> bool:
        # Checa se o grafo é completo
        edge_quantity = len(self.vertices) * (len(self.vertices)-1) / 2
        return True if self.count_edge() == edge_quantity else False