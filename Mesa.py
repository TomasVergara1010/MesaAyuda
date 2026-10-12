from cola import Cola
from pilas import Pilas
from Solicitud import Solicitud

class Mesa_Ayuda:
    
    def __init__(self):
        self.colaPendientes = Cola()
        self.pilaHistorial = Pilas()
    
    def registrarSolicitud(self):
        print("--Bienvenido al sistema para registar solicitudes--")
        
        identificador = input("Ingrese el Id de la solicitud: ")
        nombre = input("Ingrese el nombre de la persona afectada: ")
        descripcion = input("Describa el problema de forma breve: ")
        
        nuevaSolicitud = Solicitud(identificador, nombre, descripcion)
        
        self.colaPendientes.enqueue(nuevaSolicitud)
    
    def atenderSigSolicitud(self):
        print("--Atender la siguiente solicitud--")
        
        if self.colaPendientes.is_empty():
            print("No hay otra solicitud")
        
        solicitudAtendida = self.colaPendientes.dequeue()
        
        self.pilaHistorial.push(solicitudAtendida)
        print(f"Se agrego {solicitudAtendida} al historial")
    
    def consultarSolisPendientes(self):
        print("--Consulta de solicitudes pendientes--")
        
        if self.colaPendientes.is_empty():
            print("No hay solicitudes pendientes")
        
        else:
            print(self.colaPendientes())
            self.colaPendientes.mostrar()
    
    def consultarUltiSoliAtendida(self):
        print("--Consulta la ultima solicitud atendida--")
        
        if self.pilaHistorial.is_empty():
            print("No se ha atendido ninguna solicitud")
        
        else:
            ultimaSoli = self.pilaHistorial.peek()
            print(f"La ultima solicitud atendida fue: {ultimaSoli}")
        

        