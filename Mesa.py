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

        solicitudAtendida = self.colaPendientes.dequeue()
        
        if solicitudAtendida is not None:
            self.pilaHistorial.push(solicitudAtendida)
            print(f"Solicitud atendida con éxito: {solicitudAtendida}")
    
        else:
            print("No hay otra solicitud pendiente para atender.")
    
    def consultarSolisPendientes(self):
        print("--Consulta de solicitudes pendientes--")
        
        if self.colaPendientes.is_empty():
            print("No hay solicitudes pendientes")
        
        else:
            self.colaPendientes.mostrar()
    
    def consultarUltiSoliAtendida(self):
        print("--Consulta la ultima solicitud atendida--")
        
        if self.pilaHistorial.is_empty():
            print("No se ha atendido ninguna solicitud")
        
        else:
            ultimaSoli = self.pilaHistorial.peek()
            print(f"La ultima solicitud atendida fue: {ultimaSoli}")
        
    def cantidadSolisPendientes(self):
        print("--Cantidad de solicitudes pendientes--")
        
        cantidad = self.colaPendientes.size()
        print(f"Hay {cantidad} solicitudes pendientes")
        
    def ejecutar(self):
        while True:
            print("-"*40)
            print(" "*10, " Mesas de Ayuda ", " "*10)
            print("-"*40)
            
            print("1. Registrar una solicitud")
            print("2. Atender la siguiente solicitud")
            print("3. Consultar solicitudes pendientes")
            print("4. Consultar ultima solicitud atendida")
            print("5. Consultar cantidad de solicitudes pendientes")
            print("6. Salir")
            print("\n")
            
            opcion = int(input("Por favor, seleccione una opción: "))
            
            if opcion == 1:
                self.registrarSolicitud()
            elif opcion == 2:
                self.atenderSigSolicitud()
            elif opcion == 3:
                self.consultarSolisPendientes()
            elif opcion == 4:
                self.consultarUltiSoliAtendida()
            elif opcion == 5:
                self.cantidadSolisPendientes()
            elif opcion == 6:
                print("Tenga un feliz dia")
                break
            else:
                print("Error, seleccione una opcion valida")
            
            