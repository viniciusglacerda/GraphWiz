from graph import *

graph = BaseManipulation(4)
graph.create_edge(1,1)
graph.create_edge(2,2)
graph.create_edge(3,3)
graph.create_edge(4,4)
print(graph.count_edge())
graph.show_matrix()
graph.show_list()