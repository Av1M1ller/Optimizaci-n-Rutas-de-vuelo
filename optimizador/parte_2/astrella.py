

# imports
from estructuras.abierta import MinHeap
from estructuras.cerrada import TablaHash
from estructuras.nodo import Nodo


class aestrella():
    def __init__(self, inicio: Nodo, meta: Nodo):

        # listas abiertas y cerradas
        self.lista_abierta = MinHeap()
        self.lista_cerrada = TablaHash()

        # estado de inicio y fin
        self.meta = meta
        self.inicio = inicio

        self.camino = self._get_camino()

        # self.grafo = grafo()?

    # funciones principales
    def search(self):
        """
        abiertos = MinHeap()
                    abiertos.insert(inicio, prioridad = h(inicio))
                
                    g[inicio] = 0
                    padre[inicio] = None
        
        """
        nodo_inicio = self.inicio
        self.lista_abierta.insertar(nodo_inicio)

        while not self.lista_abierta.isEmpty():
            actual = self.lista_abierta.extraer_minimo()
            if actual is self.meta:
                return self.camino

            

        

    def get_info():
        pass

    # funciones secundarias
    def _expandir(self, nodo: Nodo):
        hijos = nodo.get_destinos()
        for hijo in hijos:
            self.lista_abierta.insertar(hijo)

    def _abrir():
        pass

    def _comprobar_insertar():
        pass

    def _comprobar_optimo():
        pass

    def _get_camino(self):
        pass


# ------------------------------------------------------------------------------------------

    #   ALGORITMO A* (A GRANDES RASGOS)
    #0  Casos base
# if Meta == Raiz: #FIXME
#     return Raiz
#     #1  Abrimos la raiz y la expandimos
# abiertos.append(Raiz)
#     #2  Bucle que expande (FIFO)
#     #CONDICIONES PARA PARAR:
#     #-Se han expandido toda la lista abierta
#     #-Todos los nodos tienen coste mayor que el nodo Meta:
# condicion = False
# while abiertos != [] or condicion == True:
#     heap_sort(abiertos)
#     expandir(abiertos[0])

#     if abiertos[0][1] < Meta[1] and Optimo != None:
#         condicion == False

# ------------------------------------------------------------------------------------------

"""
A*(inicio, objetivo):

    abiertos = MinHeap()
    abiertos.insert(inicio, prioridad = h(inicio))

    g[inicio] = 0
    padre[inicio] = None

    mientras abiertos no esté vacío:

        actual = abiertos.extract_min()

        si actual == objetivo:
            devolver reconstruir_camino(padre, objetivo)

        para cada vecino de actual:

            coste = g[actual] + distancia(actual, vecino)

            si vecino no está en g O coste < g[vecino]:

                padre[vecino] = actual
                g[vecino] = coste

                f = g[vecino] + h(vecino)

                abiertos.insert_or_update(vecino, prioridad = f)

    devolver None
"""