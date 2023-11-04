from graph import Graph

class DepthFirstSearch:
    def __init__(self, graph:Graph) -> None:
        self.t = 0
        self.td = {}
        self.tt = {}
        self.parent = {}
        
        for vertex in graph.vertices:
            self.td[vertex] = 0
            self.tt[vertex] = 0
            self.parent[vertex] = None
    
    def search(self):
        ...

class GraphAnalyzer:
    def depth_first_search(self, vertices_list):
        ...

    def breadth_first_search():
        ...