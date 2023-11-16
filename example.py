import random
import time
from GraphWiz import Graph
from GraphWiz.utils import print_progress_bar
import signal
import sys

def signal_handler(sig, frame):
    print("Ctrl+C pressed. Exiting...")
    sys.exit(0)

def generate_random_graph(num_vertices):
    if num_vertices <= 0:
        print("Number of vertices must be greater than zero.")
        return None

    # Create a graph
    random_graph = Graph(qtd_vertices=num_vertices)

    # Add random edges
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if random.choice([True, False]):
                # Convert indices to labels
                vertex_i_label = random_graph.vertices[i].label
                vertex_j_label = random_graph.vertices[j].label

                random_graph.create_edge(vertex_i_label, vertex_j_label)
        print_progress_bar(i+1, num_vertices, prefix='Edge Add Progress:', suffix='Complete', length=50)

    return random_graph

def measure_time(graph, method):
    start_time = time.time()
    graph.eulerian_path(method=method)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

if __name__ == "__main__":
    # Configurando o tratamento de sinal para Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    
    size = 100
    random_graph = generate_random_graph(size)

    if random_graph:
        print(f"\nTesting with {size} vertices:")
        # print("Random Graph:")
        # random_graph.show_matrix()
        # random_graph.show_list()
        # print("\n")
            
        # Measure time for Naive Method
        time_naive = measure_time(random_graph, method="naive")
        print(f"Naive Method Time: {time_naive:.6f} seconds")
        print("\n")

        # Measure time for Tarjan Method
        time_tarjan = measure_time(random_graph, method="tarjan")
        print(f"Tarjan Method Time: {time_tarjan:.6f} seconds")