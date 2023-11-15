# GraphWiz

GraphWiz is a Python library for working with graphs. It provides functionality to create, modify, and analyze graphs, as well as perform common graph algorithms. The library is designed to be flexible and user-friendly, allowing users to work with both directed and undirected graphs.

## Installation

Certainly! Installing GraphWiz without using `pip` involves manually downloading the library and including it in your Python project. Here are the steps:

1. **Download the GraphWiz Library:**
   - Go to the [GraphWiz GitHub repository](https://github.com/viniciusglacerda/GraphWiz).
   - Click on the green "Code" button, and then click "Download ZIP".
   - Extract the contents of the downloaded ZIP file to a location on your computer.

2. **Include the Library in Your Project:**
   - Copy the `GraphWiz` folder (containing the `__init__.py`, `graph.py`, `graphElements.py`, and other files) to the directory where you have your Python scripts.

3. **Use GraphWiz in Your Python Script:**
   - In your Python script, you can now import and use the `Graph` class from GraphWiz:

     ```python
     from GraphWiz import Graph

     # Create a graph
     graph = Graph(qtd_vertices=5)
     ```

   - Make sure the script and the `GraphWiz` folder are in the same directory.

4. **Run Your Script:**
   - Execute your Python script using your preferred method (command line, IDE, etc.).

This manual installation approach allows you to use GraphWiz in your project without relying on `pip`. Keep in mind that if GraphWiz has any dependencies, you might need to manually handle them as well.

## Getting Started

Here's a quick guide to help you get started with GraphWiz:

### Creating a Graph

To create a new graph, you can instantiate the `Graph` class. You can specify the number of vertices, whether the graph is directed, and provide labels for the vertices:

```python
from GraphWiz import Graph

# Create an undirected graph with 5 vertices
graph = Graph(qtd_vertices=5)

# Alternatively, you can provide labels for the vertices
graph_with_labels = Graph(qtd_vertices=5, vertices_labels=["A", "B", "C", "D", "E"])
```

### Adding Vertices and Edges

You can add vertices and edges to the graph using the following methods:

```python
# Add new vertices
graph.add_new_vertices(qtd=3, labels=["F", "G", "H"])

# Create edges between vertices
graph.create_edge("A", "B")
graph.create_edge("B", "C")
graph.create_edge("C", "A")
```

### Graph Representation

GraphWiz provides methods to display the graph's matrix and adjacency list:

```python
# Display the matrix representation of the graph
graph.show_matrix()

# Display the adjacency list representation of the graph
graph.show_list()
```

### Graph Algorithms

GraphWiz includes various graph algorithms, such as breadth-first search (BFS), depth-first search (DFS), finding bridges, and Fleury's algorithm for Eulerian paths:

```python
# Perform BFS starting from vertex "A"
levels, predecessors = graph.bfs(graph.vertex_by_label("A"))

# Find bridges in the graph using the Tarjan method
bridges = graph.bridge_tarjan_method()

# Find an Eulerian path in the graph using Fleury's algorithm
graph.eulerian_path()
```

### Saving and Loading Graphs

You can save and load graphs in the GEXF format:

```python
# Save the graph to a GEXF file
graph.to_gexf(file_path="", file_name="graph.gexf")

# Load a graph from a GEXF file
graph_from_file = Graph()
graph_from_file.from_gexf("graph.gexf")
```

## Contributing

If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on [GitHub](https://github.com/yourusername/GraphWiz).

Happy graphing with GraphWiz! 📊