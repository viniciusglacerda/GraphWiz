from graphElements import Vertex, Edge

class BaseManipulation:
    def __init__(self, vertex:int=0, is_directed:bool=False, vertex_labels:list[str]=[]) -> None:
        # Deve ser implementado a criação de um grafo com X vértices (o número de vértices deve ser inserido pelo usuário)
        self.vertex = vertex
        self.is_directed = is_directed
        self.vertex_list = [Vertex(i).set_label(vertex_labels[i]) if vertex_labels else Vertex(i) for i in range(vertex)]
        self.graph = [[Edge([i, j]) for j in range(self.vertex)] for i in range(self.vertex)]

    def show_matrix(self) -> None:
        print("    ", end="")
        [print(f"{self.vertex_list[i].get_label() if self.vertex_list[i].get_label() else self.vertex_list[i].get_index()+1}", end="  ") for i in range(len(self.vertex_list))]
        print("\n")
        for row in range(len(self.vertex_list)):
            r = self.graph[row]
            vertex = self.vertex_list[row]
            print(f"{vertex.get_label() if vertex.get_label() else vertex.get_index()+1}  {[r[i].get_weight() for i in range(len(r))]}")

    def show_list(self) -> None:
        for index, vertex in enumerate(self.vertex_list):
            label = vertex.get_label() or vertex.get_index()+1
            print(f"[{label}] ->", end=" ")
            for edge in self.graph[index]:
                if edge.get_weight():
                    v1, v2 = edge.get_vertex_pair()
                    label2 = v1.get_label() or v1.get_index()+1 if v1 != vertex else v2.get_label() or v2.get_index()+1
                    print(f"[{label2}] ->", end=" ")
            print("")
    
    def add_new_vertices(self, qtd:int=0, **kwargs) -> None:
        ...

    def remove_vertice(self) -> None:
        ...

    def create_edge(self, vertex_1:int, vertex_2:int) -> None:
        # Deve ser implementado criação de arestas
        vertex_list = self.vertex_list
        self.graph[vertex_1-1][vertex_2-1].set_weight(1)
        self.graph[vertex_1-1][vertex_2-1].set_vertex_pair([vertex_list[vertex_1-1], vertex_list[vertex_2-1]])
        if not self.is_directed:
            self.graph[vertex_2-1][vertex_1-1].set_weight(1)
            self.graph[vertex_2-1][vertex_1-1].set_vertex_pair([vertex_list[vertex_1-1], vertex_list[vertex_2-1]])
    
    def remove_edge(self, vertex_1:int, vertex_2:int) -> None:
        # Remoção de arestas
        self.graph[vertex_1-1][vertex_2-1].set_weight(0)
        self.graph[vertex_1-1][vertex_2-1].set_vertex_pair([])
        if not self.is_directed:
            self.graph[vertex_2-1][vertex_1-1].set_weight(0)
            self.graph[vertex_2-1][vertex_1-1].set_vertex_pair([])
    
    def vertex_weighting(self, vertex:int, weight:int) -> None:
        # Ponderação de vértices
        self.vertex_list[vertex-1].set_weight(weight)

    def vertex_labeling(self, vertex:int, label:str) -> None:
        # Rotulação de vértices
        self.vertex_list[vertex-1].set_label(label) 
    
    def edge_weighting(self, vertex_1:int, vertex_2:int, weight:int=1) -> None:
        # Ponderação de arestas
        self.graph[vertex_1-1][vertex_2-1].set_weight(weight)
        if not self.is_directed: self.graph[vertex_2-1][vertex_1-1].set_weight(weight)

    def edge_labeling(self, vertex_1:int, vertex_2:int, label:str) -> None:
        # Rotulação de arestas
        self.graph[vertex_1-1][vertex_2-1].set_label(label)
        self.graph[vertex_2-1][vertex_1-1].set_label(label)

    def vertex_adjacency_check(self, vertex_1:int, vertex_2:int) -> bool:
        # Checagem de adjacencia entre vertices
        verification = self.graph[vertex_1-1][vertex_2-1].get_weight()
        return True if verification else False
    
    def edge_adjacency_check(self):
        # Checagem de adjacencia entre arestas
        ...
    
    def exist_edge(self, vertex_1:int, vertex_2:int) -> bool:
        # Verifica existência de aresta
        return True if self.graph[vertex_1-1][vertex_2-1].get_weight() else False
    
    def count_edge(self) -> int:
        # Checa a quantidade de arestas
        count = 0
        for row in self.graph:
            for col in row:
                if col.get_weight():
                    count+=1
        return count
    
    def count_vertex(self) -> int:
        # Checa a quantidade de vértices
        return len(self.vertex_list)
    
    def is_empty_graph(self) -> bool:
        # Checa se o grafo é vazio
        return True if self.vertex_list else False
    
    def is_complete_graph(self) -> bool:
        # Checa se o grafo é completo
        edge_quantity = len(self.vertex_list) * (len(self.vertex_list)-1) / 2
        return True if self.count_edge() == edge_quantity else False