from GraphWiz.graph import Graph
from GraphWiz.utils import print_progress_bar

def print_menu():
    print("\nMenu:")
    print("1. Criar novo grafo")
    print("2. Adicionar vértice")
    print("3. Adicionar aresta")
    print("4. Visualizar grafo")
    print("5. Realizar busca em largura (BFS)")
    print("6. Realizar busca em profundidade (DFS)")
    print("7. Verificar se o grafo é euleriano e encontrar caminho euleriano")
    print("8. Salvar grafo em formato GEXF")
    print("9. Carregar grafo a partir de arquivo GEXF")
    print("0. Sair")

def create_graph_from_user_input():
    try:
        qtd_vertices = int(input("Digite a quantidade de vértices: "))
        is_directed = input("O grafo é direcionado? (S/N): ").upper() == 'S'
        vertices_labels = input("Digite as rótulos dos vértices separados por espaço: ").split()
        
        graph = Graph(qtd_vertices=qtd_vertices, is_directed=is_directed, vertices_labels=vertices_labels)
        print("Grafo criado com sucesso!")
        return graph
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números inteiros para a quantidade de vértices.")

def add_vertex(graph):
    try:
        qtd = int(input("Digite a quantidade de vértices a serem adicionados: "))
        labels = input("Digite os rótulos dos vértices separados por espaço: ").split()
        graph.add_new_vertices(qtd=qtd, labels=labels)
        print(f"{qtd} vértices adicionados com sucesso!")
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um número inteiro para a quantidade de vértices.")

def add_edge(graph):
    try:
        src_label = input("Digite o rótulo do vértice de origem: ")
        target_label = input("Digite o rótulo do vértice de destino: ")
        graph.create_edge(src_label, target_label)
        print(f"Aresta entre {src_label} e {target_label} adicionada com sucesso!")
    except ValueError:
        print("Rótulos de vértices inválidos. Certifique-se de que os vértices existem no grafo.")

def visualize_graph(graph):
    print("\nVisualização do Grafo:")
    print("Matriz de Adjacência:")
    graph.show_matrix()
    print("\nLista de Adjacência:")
    graph.show_list()

def bfs(graph):
    start_vertex_label = input("Digite o rótulo do vértice de início: ")
    start_vertex = graph.vertex_by_label(start_vertex_label)
    if start_vertex:
        level, predecessor = graph.bfs(start_vertex)
        print("\nResultados da BFS:")
        print("Níveis:", level)
        print("Predecessores:", predecessor)
    else:
        print("Vértice de início não encontrado.")

def dfs(graph):
    start_vertex_label = input("Digite o rótulo do vértice de início: ")
    start_vertex = graph.vertex_by_label(start_vertex_label)
    if start_vertex:
        discovery_time, finish_time, parent = graph.dfs(start_vertex)
        print("\nResultados da DFS:")
        print("Tempo de Descoberta:", discovery_time)
        print("Tempo de Finalização:", finish_time)
        print("Pais:", parent)
    else:
        print("Vértice de início não encontrado.")

def eulerian(graph):
    method = input("Escolha o método (naive/tarjan): ")
    graph.eulerian_path(method)

def save_to_gexf(graph):
    file_name = input("Digite o nome do arquivo GEXF (com a extensão .gexf): ")
    graph.to_gexf(file_name=file_name)
    print(f"Grafo salvo em {file_name}.")

def load_from_gexf(graph):
    file_path = input("Digite o caminho do arquivo GEXF: ")
    graph.from_gexf(file_path)
    print("Grafo carregado com sucesso.")

if __name__ == "__main__":
    current_graph = None

    while True:
        print_menu()
        option = input("Escolha uma opção: ")

        if option == '1':
            current_graph = create_graph_from_user_input()
        elif current_graph is not None:
            if option == '2':
                add_vertex(current_graph)
            elif option == '3':
                add_edge(current_graph)
            elif option == '4':
                visualize_graph(current_graph)
            elif option == '5':
                bfs(current_graph)
            elif option == '6':
                dfs(current_graph)
            elif option == '7':
                eulerian(current_graph)
            elif option == '8':
                save_to_gexf(current_graph)
            elif option == '9':
                load_from_gexf(current_graph)
            elif option == '0':
                print("Encerrando o programa. Até mais!")
                break
            else:
                print("Opção inválida. Tente novamente.")
        else:
            print("Crie um grafo primeiro (Opção 1).")