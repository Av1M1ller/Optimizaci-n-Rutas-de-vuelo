# la lista abierta contiene los nodos que aún no han sido expandidos.
# Es una cola creada con listas enlazadas:
# por qué una cola?: porque mantiene la propiedad de "heap", 
# que hace que el nodo de menor coste esté al inicio de la cola 
#(con una lista habría que buscarlo lo cual sería O(n))

# ----------------------------------

# por qué con listas enlazadas?, porque tendremos que insertar 
#nuevos nodos al inicio de la lista, lo cuál haría que hubiese que desplazar 
#el resto de elementos n posicones a la derecha O(n)


#------------

# por qué doblemente enlazada?: porque así las operaciones 

# -----------------
class Dnode:
    def __init__(self, e):
        self.elemento = e
        self.next = None
        self.prev = None


class Dlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, new_node):
        # con la lista doblemente enlazada nos ahorramos tener que recorrer toda la lista hasta llegar al ultimo nodo, ya que ya lo tenemos guardado como tail
        self.tail.next = new_node   
        self.new_node.prev = self.tail
        self.size += 1

    def append_left(self, new_node):
        self.head.prev = new_node
        new_node.next = self.head 
        self.head = new_node

        self.size += 1

    def pop(self) -> Dnode: #FIXME: Robustez
        tail = self.tail #WARNING: legal?

        nuevo_ultimo = self.tail.prev
        nuevo_ultimo.next = None
        self.tail.prev = None
        self.tail = nuevo_ultimo

        self.size -= 1

        return tail #WARNING: legal?

    def pop_left(self)->Dnode: #FIXME: Robustez
        head = self.elements.head
        nuevo_head = head.next  
        nuevo_head.prev = None
        head.next = None
        self.elements.head = nuevo_head

        self.size -=1

        


class lista_abierta:
    def __init__(self):
        self.elements = Dlist()

    def enqueue(self, new_node)->None:
        self.elements.end_insert(new_node)

    def dequeue(self)-> Dnode:
        eliminado = self.elements.end_pop()
        return eliminado

    def front(self):
        return self.elements.head

    def is_empty(self):
        pass
        

    def size(self):
        pass