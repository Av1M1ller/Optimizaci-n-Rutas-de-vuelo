import csv

class AdjacentVertex:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight


class Graph:
    def __init__(self, vertices: list, directed: bool): # vertices = ["MAD", "PAR", "BER", "XPL", "ACL"]
        self._vertices = {}
        for v in vertices:
            self._vertices[v] = []

        self._directed = directed

    def add_vertex(self, vertices):
        for vertex in vertices:
            self._vertices[vertex] = None

    
    def add_edge(self, start, end, weight: int = 1):
        if start not in self._vertices.keys() or end not in self._vertices.keys():
            return

        self._vertices[start].append(AdjacentVertex(end, weight))

        if not self._directed:
            self._vertices[end].append(AdjacentVertex(start, weight))

    def exist_edge(self, start: str, end: str): #start = (vértice1) ---- end = (vértice2) 

        for vertice in self._vertices[start]:
            if vertice.vertex == end:
                return vertice.weight
        return 0

    def get_adjacents(self, vertex):

        if vertex not in self._vertices:
            return []
            
        lista_vertices_conexiones = []
        lista = self._vertices[vertex]
        for adj in lista:
            lista_vertices_conexiones.append(adj.vertex)

        return lista_vertices_conexiones


    def get_origins(self, vertex):
        origins = []

        for v in self._vertices.keys():
            for adj in self._vertices[v]:
                if adj.vertex == vertex:
                    origins.append(adj.vertex)
        return origins
    





        