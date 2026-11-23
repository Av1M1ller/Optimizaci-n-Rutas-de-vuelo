

# imports
from estructuras.abierta import MinHeap
from estructuras.cerrada import TablaHash
from estructuras.nodo import Nodo


class aestrella():
    def __init__(self):

        # listas abiertas y cerradas
        self.lista_abierta = MinHeap()
        self.lista_cerrada = TablaHash()

        # estado de inicio y fin
        self.meta = Nodo()
        self.inicio = Nodo()

        self.camino = self._get_camino()

        # self.grafo = grafo()?

    # funciones principales
    def search():
        pass

    def get_info():
        pass

    # funciones secundarias
    def _expandir():
        #abrir()
        pass

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

