
        
class BaseManipulation:
    def __init__(self, vertex:int=0, is_directed:bool=False, vertex_labels:list[str]=[]) -> None:
        # Deve ser implementado a criação de um grafo com X vértices (o número de vértices deve ser inserido pelo usuário)
        self.vertex = vertex
        self.is_directed = is_directed
        self.vertex_labels = {i:vertex_labels[i] for i in range(vertex)} if vertex_labels else {}
        self.graph = [[0] * self.vertex for i in range(self.vertex)]

    def show_matrix(self) -> None:
        print("    ", end="")
        [print(f"{i+1 if not self.vertex_labels else self.vertex_labels.get(i)}", end="  ") for i in range(self.vertex)]
        print("\n")
        for row in range(self.vertex):
            print(f"{row+1 if not self.vertex_labels else self.vertex_labels.get(row)}  {self.graph[row]}")

    def show_list(self) -> None:
        for vert, row in enumerate(self.graph):
            print(f"[{vert+1 if not self.vertex_labels else self.vertex_labels.get(vert)}] ->", end=" ")
            for col, edge in enumerate(row):
                if edge:
                    print(f"[{col+1 if not self.vertex_labels else self.vertex_labels.get(col)}] ->", end=" ")
            print("")
    
    def add_new_vertices(self, qtd:int=0, **kwargs) -> None:
        ...

    def delete_vertice(self) -> None:
        ...

    def create_edge(self, vertex_1:int, vertex_2:int) -> None:
        # Deve ser implementado criação de arestas
        self.graph[vertex_1-1][vertex_2-1] = 1
        if self.is_directed: self.graph[vertex_2-1][vertex_1-1] = 1
    
    def remove_edge(self, vertex_1:int, vertex_2:int) -> None:
        # Remoção de arestas
        self.graph[vertex_1-1][vertex_2-1] = 0
        if self.is_directed: self.graph[vertex_2-1][vertex_1-1] = 0
    
    def vertex_weighting(self, vertex_1:int, vertex_2:int, weight:int) -> None:
        # Ponderação de vértices
        ...

    def vertex_labeling(self):
        # Rotulação de vértices
        ...
    
    def edge_weighting(self, vertex_1:int, vertex_2:int, weight:int=1) -> None:
        # Ponderação de arestas
        self.graph[vertex_1-1][vertex_2-1] = weight
        if self.is_directed: self.graph[vertex_2-1][vertex_1-1] = weight

    def edge_labeling(self):
        # Rotulação de arestas
        ...

    def vertex_adjacency_check(self):
        # Checagem de adjacencia entre vertices
        ...
    
    def edge_adjacency_check(self):
        # Checagem de adjacencia entre arestas
        ...
    
    def exist_edge(self, vertex_1:int, vertex_2:int) -> bool:
        # Verifica existência de aresta
        if self.graph[vertex_1-1][vertex_2-1]:
            return True
        return False
    
    def count_edge(self) -> int:
        # Checa a quantidade de arestas
        count = 0
        for row in self.graph:
            for col in row:
                if col == 1:
                    count+=1
        return count
    
    def count_vertex(self) -> int:
        # Checa a quantidade de vértices
        return self.vertex
    
    def is_empty_graph(self):
        # Checa se o grafo é vazio
        ...
    
    def is_complete_graph(self):
        # Checa se o grafo é completo
        ...

vertices = {
    vertice[int]: {
        label[str],
        weight[int],
        vizinhança[list[int|str]],
    }
}
arestas = {
    aresta[int]: {
        label[str],
        weight[int]
    }
}