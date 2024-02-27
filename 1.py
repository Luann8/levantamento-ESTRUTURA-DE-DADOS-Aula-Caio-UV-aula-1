 
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


     
