class Solicitud:
    
    def __init__(self, identificador, nombre, descripcion):
        self.identificador = identificador
        self.nombre = nombre
        self.descripcion = descripcion
    
    def __str__(self):
        return f"{self.identificador} - {self.nombre} - {self.descripcion}"

