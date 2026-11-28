


class Dnode:
    def __init__(self, e):
        self.elem = e
        self.next = None
        self.prev = None


class Dlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    
    def append(self, new_node):
        # ADD: con la lista doblemente enlazada nos ahorramos tener que recorrer toda la lista hasta llegar al ultimo nodo, ya que ya lo tenemos guardado como tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        
        self.tail.next = new_node   
        new_node.prev = self.tail
        self.tail = new_node
        self.size += 1

    def append_left(self, new_node):
        #robustez
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return


        self.head.prev = new_node
        new_node.next = self.head 
        self.head = new_node

        self.size += 1

    def pop(self) -> Dnode: #FIXME: Robustez
        tail = self.tail #WARNING: legal?

        if self.size == 0:
            return
        if self.size == 1:
            nodo_eliminado = self.head

            self.tail = None
            self.head = None
            self.size -= 1
            
            return nodo_eliminado 

        nuevo_ultimo = self.tail.prev
        nuevo_ultimo.next = None
        self.tail.prev = None
        self.tail = nuevo_ultimo

        self.size -= 1

        return tail #WARNING: legal?

    def pop_left(self)-> Dnode: #FIXME: Robustez

        if self.isEmpty():
            return
        
        if self.size == 1:
            nodo_eliminado = self.head #/self.tail
            self.tail = None
            self.head = None
            self.size-=1

            return nodo_eliminado

        head = self.head
        nuevo_head = head.next  

        nuevo_head.prev = None
        head.next = None

        self.head = nuevo_head

        self.size -=1
        return head

    def remove(self, elem): #O(n)
        node = Dnode(elem)

        nodo_actual = self.head
        if self.isEmpty():
            return
        
        if self.size == 1 and nodo_actual.elem == elem:
            self.pop_left()
            return

        while nodo_actual is not None: 
            if nodo_actual.elem == node.elem:
                if self.head == nodo_actual: # es el primer nodo
                    self.pop_left()
                    return
                if self.tail == nodo_actual:
                    self.pop()
                    return 
                else:
                    nodo_anterior = nodo_actual.prev
                    nodo_siguiente = nodo_actual.next

                    nodo_anterior.next = nodo_siguiente
                    nodo_siguiente.prev = nodo_anterior
                    self.size-=1

                    nodo_actual.next = None
                    nodo_actual.prev = None
                    return
                
            nodo_actual = nodo_actual.next

        return None

    def search(self, elem)->Dnode: #O(n)
        nodo_actual = self.head

        while nodo_actual is not None:
            if nodo_actual.elem == elem:
                return nodo_actual
    
            nodo_actual = nodo_actual.next
        
        return None



        

class TablaHash():
    def __init__(self, capacity):
        self.capacity = capacity    #número de buckets de la tabla                       
        self.size = 0   # número de elementos en cada bucket
        self.table = [None] * self.capacity

    def show(self):
        print(self.table)
        
    def hash_function(self, elem):
        return elem % self.capacity

    def search(self, elem) -> Dnode: # ADD: Búsqueda O(1+alpha) 
        posicion = self.hash_function(elem)
        dlist_bucket = self.table[posicion] 
        if dlist_bucket is None:
            return
        
        return dlist_bucket.search(elem) 



    def insert(self, elem):
        # comprobar tipado para evitar error
        posicion_bucket = self.hash_function(elem) # sintaxis a raíz del método mágico
        print(f"posicion en el bucket: {posicion_bucket}")

        if self.table[posicion_bucket] is None:
            self.table[posicion_bucket] = Dlist()
            self.table[posicion_bucket].append(Dnode(elem)) #TODO: Cambiar método append para que solo haya que pasar un elemento?
            self.size += 1

        elif self.table[posicion_bucket] is not None: # ya hay una lista enlazada
            self.table[posicion_bucket].append(Dnode(elem))
            self.size += 1

        else:
            print("What?, ha ocurrido otra cosa")


    def delete(self, elem):

        posicion_bucket = self.hash_function(elem)
        bucket = self.table[posicion_bucket]

        if bucket is None:
            return
        if bucket.search(elem) is None:
            return
        
        bucket.remove(elem)

        
        self.size -= 1
        