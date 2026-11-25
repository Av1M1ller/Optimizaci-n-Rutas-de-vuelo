from dataclasses import dataclass


class aeropuerto:
    def __init__(self, codigo_aeropuerto):
        self.codigo_aeropuerto = codigo_aeropuerto
        self.destinos = [] # lista de objetos destino : (codigo_aeropuerto_destino, distancia haversine)


        
class destinos:
    def __init__(self, IATA_destino):
        self.IATA = IATA_destino
        self.coste = self.obtener_coste()
        
    def obtener_coste(self)-> int:
        pass


class grafo:
    def __init__(self):
        self.padre 

# ------------------------------------------------------------------------------------------
    #   A*
    #   Definir objeto aeropuerto inicial (Nodo) FIXME
Raiz = (IATA, 0, "")

    #   Definir estado meta (aeropuerto al que quieres llegar) FIXME
Meta =  (IATA, -1, "")

    #   Optimo: se guarda aqui el nodo meta al que se ha llegado con menor coste. 

Optimo = None
    #   Abiertos: lista de tuplas
#   Contiene todos los nodos a los que hemos llegado y no han sido expandidos
#   tupla(nodo, coste, su padre)
abiertos = [] 

#   Expandidos: lista de tuplas que contiene la tupla que sale de abiertos
Expandidos = []

# ------------------------------------------------------------------------------------------

    #   coste f = g + h
def costeTotal(g, h):
    return g + h

# ------------------------------------------------------------------------------------------

#   def abrir: crea los hijos de un padre y los mete al fianl de lista abierta
def abrir(padre):
    for destinos in range(nodo.destinos): # :O       FIXME: h aun no esta definido
        #padre[1] = coste del padre
        #padre[0] = IATA del padre (no puede hacer dos iguales)
        hijo = (destinos.IATA, costeTotal(destinos.coste, h) + padre[1], padre[0]) #coste actaul + coste del padre
        comprobRepetidos(hijo) #Si no está repetido lo añade
        comprobarMeta(hijo)

# ------------------------------------------------------------------------------------------

#   def comprobRepetidos: si en la suma de Abiertos y Expandidos hay un nodo repetido se borra el de coste mayor
def comprobRepetidos(nodo): #FIXME:optimizable
    for i in range(abiertos): #FIXME: verificando solo en la lista de cerrados ya es suficiente????
        noRepet = True
        if nodo(0) == i[0]:
            if nodo[1] < i[1]: #Nodo válido para entrar (si se cumple no hay que revisar Expandidos)
                abiertos.pop(i)
                abiertos.append(nodo)
            else:
                noRepet = False

    for j in range(Expandidos): #TODO: Implementar búsqueda con tabla hash O(1) vs O(n)
        if nodo(0) == j[0]:
            if nodo[1] < j[1]: #Nodo válido para entrar
                abiertos.pop(j)
                abiertos.append(nodo)
            else:
                noRepet = False
    if noRepet == True:
        abiertos.append(nodo)

# ------------------------------------------------------------------------------------------

#   Def Expandir: sacar primer nodo de abiertos y meter sus hijos al final (FIFO)
def expandir(nodo):
    aux = abiertos.pop(0)
    Expandidos.append(aux)
    abrir(nodo)

# ------------------------------------------------------------------------------------------

#   Def ComprobarMeta: comprueba si el nodo es meta FIXME
def comprobarMeta(nodo):
    if nodo[0] == Meta and Optimo == None: #Primera vez que se llega a la meta
        Optimo = nodo
    elif nodo[1] < Optimo[1]: #Mejor camino para llegar a la meta
        Optimo = nodo

# ------------------------------------------------------------------------------------------

#   ALgoritmo de ordenacion por montículos binarios:
def heapify(lista, n, i):
    mayor = i
    izq = 2 * i + 1
    der = 2 * i + 2

    if izq < n and lista[izq][1] > lista[mayor][1]:
        mayor = izq

    if der < n and lista[der][1] > lista[mayor][1]:
        mayor = der

    if mayor != i:
        lista[i], lista[mayor] = lista[mayor], lista[i]
        heapify(lista, n, mayor)


def heap_sort(lista):
    n = len(lista)

    # Construir el montículo máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    # Extraer los elementos del montículo
    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        heapify(lista, i, 0)

    return lista

# ------------------------------------------------------------------------------------------

    #   ALGORITMO A* (A GRANDES RASGOS)

    #0  Casos base
if Meta == Raiz: #FIXME
    return Raiz
    #1  Abrimos la raiz y la expandimos
abiertos.append(Raiz)

    #2  Bucle que expande (FIFO)
    #CONDICIONES PARA PARAR:
    #-Se han expandido toda la lista abierta
    #-Todos los nodos tienen coste mayor que el nodo Meta:
condicion = False
while abiertos != [] or condicion == True:
    heap_sort(abiertos)
    expandir(abiertos[0])

    if abiertos[0][1] < Meta[1] and Optimo != None:
        condicion == False

# ------------------------------------------------------------------------------------------