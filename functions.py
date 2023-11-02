from Equipo import*
import re
#esta es mi biblioteca de funciones.En este modulo separe una funciones de validacion.
#esta funcion recibe un str
#valida la opcion
#devuelve un booleano
def validar_opcion_numero(opcion):
    try:
        opcion_numero = int(opcion)
        if 1 <= opcion_numero <= 9:
            return True
        else:
            return False
    except ValueError:
        return False
    
"""
La función `validar_jugador_por_nombre` comprueba si un nombre dado es válido comparándolo con un
patrón de expresión regular.
    
:param nombre: El parámetro "nombre" es una cadena que representa el nombre de un jugador
escriba nombre: str
:return: un valor booleano, ya sea Verdadero o Falso."""
def validar_jugador_por_nombre(nombre:str):
   
    resultado = False
    if re.match(r"^[a-zA-Z\s\'-]+ [a-zA-Z\s\'-]+$", nombre):
       resultado = True
    else:
        print("Nombre inválido. Respete los nombres tal cual estan en la lista.")
    return resultado
def lista_de_jugadores_nombres():
    """
    La función "lista_de_jugadores_nombres" imprime los nombres y posiciones de los jugadores de un equipo.
    """
    for i, jugador in enumerate(equipo.jugadores):
        print(f"{i+1} . {jugador['nombre']} - {jugador['posicion']}")
def validar_opcion_submenu(opcion):
    """
   La función "validar_opcion_submenu" comprueba si una opción determinada es una opción de submenú válida.
    
     :param opcion: El parámetro "opción" es la opción de entrada que necesita ser validada. debería ser un
     cadena que representa un número
     :return: un valor booleano. Devuelve True si la entrada "opción" es una opción de submenú válida (una
     entero entre 1 y 3), y False en caso contrario.
    """
    try:
        opcion_numero = int(opcion)
        if 1 <= opcion_numero <= 3:
            return True
        else:
            return False
    except ValueError:
        return False
    
def sub_menu_punto_8():
    '''simplemente muestra un submenu
    '''
    print("1 - Ordenar los jugadores por el valor sumado.")
    print("2 - Ordenar los jugadores por porcentaje.")
    print("3 - .\n")