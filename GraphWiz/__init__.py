from graph import *

graph = Graph(5, is_directed=False)
graph.create_edge(1,2)
graph.create_edge(1,5)
graph.create_edge(2,5)
graph.create_edge(2,4)
graph.create_edge(2,3)
graph.create_edge(3,4)
graph.create_edge(4,5)

graph.add_new_vertices(qtd=2, labels=["A", "B"])
# graph.remove_vertice("A")

graph.show_matrix()
graph.show_list()

# print(graph.is_complete())
# graph.vertex_labeling(1, "T")
# print(graph.count_edge())
# graph.edge_weighting("T", 2, 3)

print(graph.bfs())