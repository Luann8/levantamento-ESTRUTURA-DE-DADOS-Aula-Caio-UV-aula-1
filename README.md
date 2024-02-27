  <h1>1- Forneça um algoritmo para encontrar o caminho mais
confiável entre dois dispositivos dados

</h1>

   <pre> <code>
import heapq

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name):
        if name not in self.vertices:
            self.vertices[name] = {}

    def add_edge(self, from_vertex, to_vertex, reliability):
        self.vertices[from_vertex][to_vertex] = reliability

    def dijkstra(self, start, end):
        heap = [(0, start)]
        visited = set()
        while heap:
            (reliability, current_vertex) = heapq.heappop(heap)
            if current_vertex in visited:
                continue
            visited.add(current_vertex)
            if current_vertex == end:
                return reliability
            for neighbor, edge_reliability in self.vertices[current_vertex].items():
                if neighbor not in visited:
                    heapq.heappush(heap, (reliability * edge_reliability, neighbor))
        return None

if __name__ == "__main__":
    network = Graph()
    network.add_vertex('A')
    network.add_vertex('B')
    network.add_vertex('C')
    network.add_vertex('D')

    network.add_edge('A', 'B', 0.9)  
    network.add_edge('A', 'C', 0.8)
    network.add_edge('B', 'D', 0.7)
    network.add_edge('C', 'D', 0.6)

    start_device = 'A'
    end_device = 'D'
    reliability = network.dijkstra(start_device, end_device)
    if reliability is not None:
        print(f"O caminho mais confiável de {start_device} para {end_device} tem uma confiabilidade de {reliability}.")
    else:
        print(f"Não há caminho possível de {start_device} para {end_device}.")


    </code> </pre>

  <h1>2- Como encontrar o fluxo máximo de passageiros entre as duas cidades?</h1>

  <pre><code>
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(dict)
        self.vertices = vertices

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity
        self.graph[v][u] = 0  # Back edge capacity is initialized as 0

    def bfs(self, s, t, parent):
        visited = [False] * self.vertices
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for v in range(self.vertices):
                if visited[v] == False and self.graph[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

        return True if visited[t] else False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.vertices
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

# Exemplo de uso:
if __name__ == "__main__":
    graph = Graph(6)  

    graph.add_edge(0, 1, 16)
    graph.add_edge(0, 2, 13)
    graph.add_edge(1, 2, 10)
    graph.add_edge(1, 3, 12)
    graph.add_edge(2, 1, 4)
    graph.add_edge(2, 4, 14)
    graph.add_edge(3, 2, 9)
    graph.add_edge(3, 5, 20)
    graph.add_edge(4, 3, 7)
    graph.add_edge(4, 5, 4)

    source = 0
    sink = 5

    max_flow = graph.ford_fulkerson(source, sink)
    print("O fluxo máximo de passageiros entre as cidades é:", max_flow)

    </code></pre>

  <h1>3. Ir de Arad até Bucharest. Qual seria o menor caminho?</h1>

  <img src="https://github.com/Luann8/levantamento-ESTRUTURA-DE-DADOS-Aula-Caio-UV-aula-1/assets/133384636/89ae1631-0e4c-462f-8c81-30e21ff6b4d2" alt="imagem">
</body>
