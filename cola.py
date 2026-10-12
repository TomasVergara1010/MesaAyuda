from Node import Node
class Cola:
    def __init__(self):
        self.frente = None
        self.final = None

    def is_empty(self):
        return self.frente is None

    def enqueue(self, data):
        nuevo = Node(data)
        if self.is_empty():
            self.frente = nuevo
        else:
            self.final.next = nuevo
        self.final = nuevo

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.frente.data
        self.frente = self.frente.next
        if self.frente is None:
            self.final = None
        return data
    
    def mostrar(self):
        if self.is_empty():
            print("No hay solicitudes pendientes")
            return
        
        actual = self.frente
        print("Solicitudes pendientes:")
        while actual is not None:
            print(actual.data)
            actual = actual.next

    
    def size(self):
        contador = 0
        actual = self.frente
        while actual is not None:
            contador += 1
            actual = actual.next
        return contador