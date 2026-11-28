

import csv
from optimizador.estructuras.grafo import AdjacentVertex
from optimizador.estructuras.grafo import Graph


def main():

    #1 Rellenar self._vertices leyendo vertices.csv
    vertices = []
    with open("dataframes/vertices.csv", mode="r", encoding="utf-8", newline="") as f:
        for fila in csv.DictReader(f):
            vertices.append(fila["acronym"])


    grafo = Graph(vertices, True)


    #2 Rellenar las aristas leyendo edges.csv (sin bucles ni vuelos duplicados)
    with open("dataframes/edges.csv", mode="r", encoding="utf-8", newline="") as f:
        for fila in csv.DictReader(f):
            origen = fila["origin"]
            destino = fila["destination"]
            distancia = float(fila["haversine_km"])

            # Evitamos bucles a sí mismo y aristas repetidas del multigrafo
            if origen != destino and grafo.exist_edge(origen, destino) == 0:
                grafo.add_edge(origen, destino, distancia)

    print("fin de la función main")


main()