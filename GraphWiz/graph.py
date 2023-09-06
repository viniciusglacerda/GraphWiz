class BaseManipulation:
    def __init__(self) -> None:
        pass

    def create_graph(self):
        # Deve ser implementado a criação de um grafo com X vértices (o número de vértices deve ser inserido pelo usuário)
        ...
    
    def create_edge(self):
        # Deve ser implementado criação de arestas
        ...
    
    def remove_edges(self):
        # Remoção de arestas
        ...
    
    def vertex_weighting(self):
        # Ponderação de vértices
        ...

    def vertex_labeling(self):
        # Rotulação de vértices
        ...
    
    def edge_weighting(self):
        # Ponderação de arestas
        ...

    def edge_labeling(self):
        # Rotulação de arestas
        ...

    def vertex_adjacency_check(self):
        # Checagem de adjacencia entre vertices
        ...
    
    def edge_adjacency_check(self):
        # Checagem de adjacencia entre arestas
        ...
    
    def exist_edge(self):
        # Verifica existência de aresta
        ...
    
    def count_edge(self):
        # Checa a quantidade de arestas
        ...
    
    def count_vertex(self):
        # Checa a quantidade de vértices
        ...
    
    def is_empty_graph(self):
        # Checa se o grafo é vazio
        ...
    
    def is_complete_graph(self):
        # Checa se o grafo é completo
        ...