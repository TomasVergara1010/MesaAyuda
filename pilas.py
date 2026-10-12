from Node import Node
class Pilas:
    def __init__(self):
        self.cima = None

    def is_empty(self):
        return self.cima is None

    def push(self, dato):
        nuevo = Node(dato)
        nuevo.siguiente = self.cima
        self.cima = nuevo

    def pop(self):
        if self.is_empty():
            return None
        dato = self.cima.dato
        self.cima = self.cima.siguiente
        return dato

    def peek(self):
        if self.is_empty():
            return None
        return self.cima.dato