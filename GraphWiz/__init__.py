from graph import *

graph = BaseManipulation(4, is_directed=True, vertex_labels=["A", "B", "C", "D"])
graph.create_edge(1,2)
graph.create_edge(2,3)
graph.create_edge(3,4)
graph.create_edge(3,2)
graph.create_edge(3,1)
graph.create_edge(4,1)
graph.vertex_labeling(1, "T")
print(graph.count_edge())
graph.show_matrix()
graph.show_list()
graph.edge_weighting(1, 2, 2)