
<div style="display: inline_block"><br>
 <img align="center" alt="python" height="60" width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" />
 <img align="center" alt="univassouras" height="60" width="60" src="https://github.com/Luann8/Web_Programming_Laboratory-Univassouras/blob/main/universidade%20de%20vassouras%20Vertical.svg" >

</div>

  
  
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
    network.add_vertex()

    network.add_edge()  

    start_device = ''
    end_device = ''
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

if __name__ == "__main__":
    graph = Graph()  

    graph.add_edge()

    source = 
    sink = 

    max_flow = graph.ford_fulkerson(source, sink)
    print("O fluxo máximo de passageiros entre as cidades é:", max_flow)

    </code></pre>

  <h1>3. Ir de Arad até Bucharest. Qual seria o menor caminho?</h1>

  <img src="https://github.com/Luann8/levantamento-ESTRUTURA-DE-DADOS-Aula-Caio-UV-aula-1/blob/main/3.jpg" alt="imagem">
</body>
