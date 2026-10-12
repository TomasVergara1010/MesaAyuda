from Node import Node
class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def is_empty(self):
        return self.frente is None

    def enqueue(self, dato):
        nuevo = Node(dato)
        if self.is_empty():
            self.frente = nuevo
        else:
            self.final.siguiente = nuevo
        self.final = nuevo

    def dequeue(self):
        if self.is_empty():
            return None
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return dato