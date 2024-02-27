
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

    
