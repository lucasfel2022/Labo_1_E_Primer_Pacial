import json

class Equipo():
    def __init__(self,archivo) -> None:
        self.archivo = archivo
        self.jugadores = []
        
    def leer_archivo(self):
        with open(self.archivo,"r",encoding="utf-8") as lista_jugadores:
            datos = json.load(lista_jugadores)
            return datos
           
        
    def mostrar_jugadores(self,datos:list):
         for jugador in datos["jugadores"]:
             print(jugador)
            
            
 #Setter y Getter
 
@property
def getArchivo(self):
    return self.getArchivo

def getJugadores(self):
    return self.getjugadores

def setArchivo(self,Archivo):
    self.setArchivo = Archivo

def setJugadores(self,jugadores):
    self.setJugadores = jugadores
    
    
               
            
equipo = Equipo("Primer_Parcial__1_E.py\Dream_Team.json")
datos = equipo.leer_archivo()
equipo.mostrar_jugadores(datos)