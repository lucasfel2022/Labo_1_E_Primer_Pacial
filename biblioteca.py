from Equipo import *
class Biblioteca:
    def __init__(self):
        # Crear una instancia de ClaseA
        self.instancia_Equipo = Equipo()

    def obtener_datos_Equipo(self):
        resultado = self.instancia_Equipo.mostrar_jugadores()
        return  resultado
    
    
def menu_opciones():
    while True:
        print("/n Menú del Dream Team:")
        print("1. Mostrar la lista de todos los jugadores del Dream Team con el formato: Nombre Jugador - Posición.")
        print("2. ")
        print("3. ")
        print("4. ")
        print("5. ")
        print("6. ")
        print("7. ")
        opcion = input("Seleccione una opción: ")
      
        if validar_opcion_numero(opcion):
            print("Opción válida.")
            match opcion:
                case 1:
                    resultado = Biblioteca.obtener_datos_Equipo()
                    print(resultado)
                    #print(resultado)
                    break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")  

def validar_opcion_numero(opcion):
    try:
        opcion_numero = int(opcion)
        if 1 <= opcion_numero <= 7:
            return True
        else:
            return False
    except ValueError:
        return False
    