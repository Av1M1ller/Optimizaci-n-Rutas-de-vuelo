
from estructuras.abierta import Nodo
# consula del elemento mínimo = o(1) vs o(logn) de un ABB


class MinHeap(): # TODO: Implementar min_heap
    def __init__(self):
        self.heap = []

    def insertar(self, objeto): # O(log(n))?
        self.heap.append(objeto)
        self._subir(len(self.heap) - 1)

    def extraer_minimo(self) -> Nodo: # O(log(n))
        if not self.heap:
            return None

        minimo = self.heap[0]
        ultimo = self.heap.pop()

        if self.heap:
            self.heap[0] = ultimo
            self._bajar(0)

        return minimo

    def _subir(self, i):
        while i > 0:
            padre = (i - 1) // 2

            if self.heap[i].costes < self.heap[padre].costes:
                self.heap[i], self.heap[padre] = self.heap[padre], self.heap[i]
                i = padre
            else:
                break

    def _bajar(self, i):
        n = len(self.heap)

        while True:
            menor = i
            izq = 2 * i + 1
            der = 2 * i + 2

            if izq < n and self.heap[izq].costes < self.heap[menor].costes:
                menor = izq

            if der < n and self.heap[der].costes < self.heap[menor].costes:
                menor = der

            if menor != i:
                self.heap[i], self.heap[menor] = self.heap[menor], self.heap[i]
                i = menor
            else:
                break

    def esta_vacio(self):
        return len(self.heap) == 0

    def __len__(self):
        return len(self.heap)


