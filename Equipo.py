import json
import re
from jugador import *
from estadisticas import *
import csv
import sqlite3
ruta_json = "Primer_Parcial__1_E.py//dream_team.json"

class Equipo():
    def __init__(self,ruta_json:str) -> None:
        """
        La función inicializa un objeto con una lista de reproductores leídos de un archivo JSON.
        
        :parametro ruta_json: El parámetro "ruta_json" es una cadena que representa la ruta a un archivo JSON
        :escribe ruta_json: str
        """
        self.jugadores = self.leer_archivo(ruta_json)
        
    def leer_archivo(self,ruta_json):
        """
        La función lee un archivo JSON y devuelve una lista de datos de los jugadores si existe; de lo contrario,
         devuelve una lista vacía.
        
        :parametro ruta_json: El parámetro "ruta_json" es una cadena que representa la ruta a un archivo JSON
        :return: una lista de jugadores. Si la clave "jugadores" está presente en el archivo JSON y su valor es
         una lista, entonces la función devuelve esa lista. De lo contrario, devuelve una lista vacía.
        """
        with open(ruta_json,"r",encoding="utf-8") as lista_jugadores:
            datos = json.load(lista_jugadores)
            if "jugadores" in datos and isinstance(datos["jugadores"], list):
                return datos["jugadores"]
            else:
                return []
        
    def mostrar_nombre_Y_posicion(self,lista_jugadores:list):
        """
       La función toma una lista de jugadores e imprime sus nombres y
         posiciones.
        
        lista_jugadores representan a los jugadores. Cada diccionario debe tener
         los atributos'nombre' y 'posicion' para almacenar el nombre y posición del jugador respectivamente
        """
        for jugador in lista_jugadores:
            print(f"{jugador['nombre']} - {jugador['posicion']}")
        


       
    def inicializar_equipo(self):
        """
        La función "inicializar_equipo" inicializa un equipo leyendo datos de un archivo JSON y
        mostrando el nombre y la posición del equipo mediante sus respectivas funciones.
        """
        datos = equipo.leer_archivo(ruta_json)
        equipo.mostrar_nombre_Y_posicion(datos)
    
    def mostrar_estadistica_jug_y_guardar_en_csv(self):
        for i, jugador in enumerate(equipo.jugadores):
            print(f"{i+1} . {jugador['nombre']} - {jugador['posicion']}")
        try:
            player =input('/n Numero del 1 al 12 /n')
            if re.match(r'^[0-9]{1,2}$', player) and 0 <= int(player) < len(equipo.jugadores):
                jugador_encontrado = equipo.jugadores[int(player) -1]
                print(jugador_encontrado)
            else:
                raise ValueError("El número ingresado no está en el rango válido.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
        respuesta = input("¿Desea guardar los datos en un archivoo csv? s/n\n").lower()
        if respuesta == "s":
            while True:
                nombre_archivo = input("Ingrese el nombre del archivo csv: ")

                if nombre_archivo.endswith(".csv"):
                
                 # El nombre del archivo termina en ".csv", es válido
                    print("Nombre de archivo válido:", nombre_archivo)
                    headers = ["nombre",
                    "posicion",
                    "temporadas",
                    "puntos_totales",
                    "promedio_puntos_por_partido",
                    "rebotes_totales",
                    "promedio_rebotes_por_partido",
                    "asistencias_totales",
                    "promedio_asistencias_por_partido",
                    "robos_totales",
                    "bloqueos_totales",
                    "porcentaje_tiros_de_campo",
                    "porcentaje_tiros_libres",
                    "porcentaje_tiros_triples",]
                    
                    with open(f"{nombre_archivo}.csv", mode="w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow(headers)
                    writer.writerow(
                    [
                        jugador_encontrado['nombre'],
                        jugador_encontrado['posicion'],
                        jugador_encontrado['estadisticas'] ['temporadas'],
                        jugador_encontrado['estadisticas']['puntos_totales'],
                        jugador_encontrado['estadisticas']['promedio_puntos_por_partido'],
                        jugador_encontrado['estadisticas']['rebotes_totales'],
                        jugador_encontrado['estadisticas']['promedio_rebotes_por_partido'],
                        jugador_encontrado['estadisticas']['asistencias_totales'],
                        jugador_encontrado['estadisticas']['promedio_asistencias_por_partido'],
                        jugador_encontrado['estadisticas']['robos_totales'],
                        jugador_encontrado['estadisticas']['bloqueos_totales'],
                        jugador_encontrado['estadisticas']['porcentaje_tiros_de_campo'],
                        jugador_encontrado['estadisticas']['porcentaje_tiros_libres'],
                        jugador_encontrado['estadisticas']['porcentaje_tiros_triples'],
                    ]
                )
        else:
         print("El archivo no se guardo")  # Sale del bucle while
    
    def buscar_jugador_por_indice(indice):
        """
        La función busca un jugador en la lista de jugadores de un equipo en función
         en su índice.
        
         El parámetro "indice" es un número entero que representa el índice del reproductor que
         quiero buscar en la lista de "equipo.jugadores"
          y retorna el jugador en el índice especificado en la lista de "equipo.jugadores".
        """
        for i, jugador in enumerate(equipo.jugadores):
            if i == indice:
                return jugador
    
    def buscar_jugador_por_nombre(self,nombre_a_buscar:str):
        """
        La función busca un jugador de un equipo por su nombre e imprime sus logros.
        
         El parámetro "nombre_a_buscar" es una cadena que representa el nombre de
         el jugador que quieres buscar
         e imprime la variable nombre_a_buscar
        """
        for jugador in equipo.jugadores:
            if re.search(nombre_a_buscar, jugador['nombre'], re.IGNORECASE):
                print(f"Logros de {jugador['nombre']}:")
                for logro in jugador['logros']:
                    print(logro)   
                    
    def calcular_promedio_puntos_x_partido(self):
        # Calcula el promedio de puntos por partido de todo el equipo
        total_puntos = sum(jugador['estadisticas']['promedio_puntos_por_partido'] for jugador in equipo.jugadores)
        promedio = total_puntos / len(equipo.jugadores)

        # Ordena la lista de jugadores por nombre de manera ascendente
        jugadores_ordenados = sorted(equipo.jugadores, key=lambda jugador: jugador['nombre'])

        # Muestra el promedio y la lista ordenada de jugadores
        print(f"Promedio de puntos por partido del equipo: {promedio}")
        print("Jugadores ordenados por nombre:")
        for jugador in jugadores_ordenados:
            print(f"{jugador['nombre']}: {jugador['estadisticas']['promedio_puntos_por_partido']} puntos por partido")
            
            
    def mostrar_miembros_del_Salon_de_la_Fama_de_Baloncesto(self,nombre_jugador):
        """
         La función "mostrar_miembros_del_Salon_de_la_Fama_de_Baloncesto" comprueba si
         El jugador es miembro del Salón de la Fama del Baloncesto e imprime el resultado.
         El parámetro "nombre_jugador" es una cadena que representa el nombre de un
         jugador de baloncesto
        """
        for jugador in equipo.jugadores:
            if jugador['nombre'] == nombre_jugador:
                for logro in jugador['logros']:
    #aca itera sobre sus atributos logros y verifica que jugador es miembro de cada sector, si de la dama o univerrsitario
                     if ("Miembro del Salon de la Fama del Baloncesto" in logro and "Universitario" not in logro):
                        print(f"{nombre_jugador} es miembro del Salón de la Fama del Baloncesto.")
                        break
                else:
                    print(f"{nombre_jugador} no es miembro del Salón de la Fama del Baloncesto.")
                    
    def calcular_maximo_rebotes_totales(self):
        """
        La función calcula el jugador con mayor rebote total en el dream team e imprime
        su nombre.
        """
        jugador_con_mas_rebotes = max(equipo.jugadores, key=lambda jugador: jugador['estadisticas']['rebotes_totales'])
        print(f"\n El jugador con mas rebotes totales de todo el dream team es: {jugador_con_mas_rebotes}")
        
        
#ordena de mayor a menor, recibe un euquipo de calse Equipo y devuelve la lista ordenada
#el metod sorted, recibe el dato de tipo 'Equipo' donde tengo mi lista jugdaores, paso parametros a buscar y me la ordena con el
#revers.
    def ordenamiento_mayor_a_menor_guardar_json_y_sqlite(self):
        """
       La función ordena una lista de diccionarios en orden descendente según una clave específica, solicita
         el usuario guarda los datos en un archivo CSV, le solicita que guarde la lista ordenada en un JSON
         y finalmente guarda los datos en una base de datos SQLite.
        """
        lista_ordenada = sorted(equipo.jugadores, key=lambda x: x['estadisticas']['puntos_totales'], reverse=True)
    # Ordena la lista de diccionarios de mayor a menor según "puntos_totales" (puedes usar la función mencionada anteriormente)
        print(f"La lista se ha ordernado segun los criterios: {lista_ordenada}")
        respuesta_csv = input("¿Desea guardar los datos en un archivoo csv? s/n\n").lower()
        if validar_opcion_respuesta(respuesta_csv) is True:
            while True:
                nombre_archivo = input("Ingrese el nombre del archivo csv: ")
                if nombre_archivo.endswith(".csv"):
        # El nombre del archivo termina en ".csv", es válido
                    print("Nombre de archivo válido:", nombre_archivo)
        else:
            print("El archivo no se guardo")  # Sale del bucle while
        respuesta_json = input("\n ¿Desea guardar la lista ordenada en un archivo json? s/n : ")
        if validar_opcion_respuesta(respuesta_json) is True:
            guardar_archivo_json(lista_ordenada)
        print("subiendo datos a la base de datos.....un momento...\n")
        guardar_lista_jugadores_en_sqlite()
        print("Los datos se han almacenado en la base datos\n")

    

def sumar_robos_y_bloqueos(self):
    """
    La función calcula la suma de robos y bloqueos de cada jugador de un equipo y devuelve una lista de
     las sumas.
     :return: una lista llamada "lista_robos_y_bloqueos" que contiene la suma de "robos_totales" y
     "bloqueos_totales" para cada jugador del equipo
    """
    lista_robos_y_bloqueos = []
    for jugador in equipo.jugadores:
        suma = jugador["estadisticas"]["robos_totales"] + jugador["estadisticas"]["bloqueos_totales"]
        lista_robos_y_bloqueos.append(suma)
    return lista_robos_y_bloqueos


def mostrar_orden_de_robos_y_bloqueos():
    """
    La función ordena los jugadores de un equipo en función de la suma de
     sus robos y bloqueos totales, y luego imprime sus nombres junto con sus respectivos robos y
     estadísticas de bloque.
    """
    jugadores_ordenados =  sorted(equipo.jugadores, key=sumar_robos_y_bloqueos, reverse=True)
    print("Jugadores ordenados por suma de robos totales y bloqueos totales: \n")
    for jugador in jugadores_ordenados:
        print(f"{jugador['nombre']}: |Robos Totales = {jugador['estadisticas']['robos_totales']}| Bloqueos Totales = {jugador['estadisticas']['bloqueos_totales']}| Suma = {sumar_robos_y_bloqueos(jugador)}")

def mostrar_jugadores_ordenados_con_porcentaje():
    '''
    como primera instancia, ordena a la lista jugadores usando el metodo sorted, que recibe una lista, un parametro osea la key
    y por ultimo utiliza el reverse como funcion de parametro tambien. para que se ordenen de mayor a menor
    '''
    jugadores_ordenados = sorted(equipo.jugadores, key=sumar_robos_y_bloqueos, reverse=True)
    ''' La linea `max_valor está calculando el
     valor máximo de la suma de "robos_totales" y "bloqueos_totales" para todos los jugadores del equipo. Él
     itera sobre cada jugador en la lista "equipo.jugadores", accede a su diccionario "estadisticas",
     y suma los valores de "robos_totales" y "bloqueos_totales". La función `suma()` luego calcula
    la suma total de estos valores. 
    '''
   
    max_valor = sum(jugador["estadisticas"]["robos_totales"] + jugador["estadisticas"]["bloqueos_totales"] for jugador in equipo.jugadores)
    print("Jugadores ordenados por suma de robos totales y bloqueos totales:")
    for jugador in jugadores_ordenados:
        suma = jugador["estadisticas"]["robos_totales"] + jugador["estadisticas"]["bloqueos_totales"]
        porcentaje = porcentaje = (suma / max_valor) * 100
        print(f"{jugador['nombre']}: |Robos Totales = {jugador['estadisticas']['robos_totales']}| Bloqueos Totales = {jugador['estadisticas']['bloqueos_totales']}| Suma = {sumar_robos_y_bloqueos(jugador)}| Porcentaje = {porcentaje:.2f}%")


def validar_opcion_respuesta(opcion):
        if opcion.lower() == 's':
            return True
        elif opcion.lower() == 'n':
            return False
        else:
            return False
    
def guardar_archivo_json(lista:list):
    with open('lista_ordenada.json','w',) as file:
        json.dump(lista,file,indent=5)
        
def guardar_lista_jugadores_en_sqlite():
        """
        La función "guardar_lista_jugadores_en_sqlite" se conecta a una base de datos SQLite, crea una tabla si
        no existe, ordena una lista de jugadores usando Quick Sort e inserta los datos de los jugadores ordenados en
        la mesa.
        """
        # Conecta a la base de datos SQLite
        conn = sqlite3.connect("Dream_Team.db")
        cursor = conn.cursor()

        # Crea una tabla si no existe
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS jugadores (
                nombre TEXT,
                posicion TEXT,
                puntos_totales FLOAT
            )
        """
        )
        jugadores_ordenados = quick_sort(equipo.jugadores)

        # Ordena la lista de jugadores con Quick Sort
       

        try:
            # Inserta los datos en la tabla
            for jugador in jugadores_ordenados:
                cursor.execute(
                    """
                    INSERT INTO jugadores (nombre, posicion, puntos_totales)
                    VALUES (?, ?, ?)
                """,
                    (jugador['nombre'], jugador['posicion'], jugador['estadisticas']['puntos_totales']),
                )

            # Guarda los cambios en la base de datos
            conn.commit()

            print("Lista de jugadores ordenada y guardada en SQLite.")
        except Exception as e:
            print(f"Error al guardar la lista de jugadores en SQLite: {str(e)}")
        finally:
            # Cierra la conexión a la base de datos
            conn.close()
def quick_sort(dict):
            """
     La función `quick_sort` implementa el algoritmo de clasificación rápida para ordenar una lista de diccionarios según
     el valor de la clave 'puntos_totales' en el diccionario 'estadisticas'.
    
      El parámetro `arr` es una lista de diccionarios. Cada diccionario representa una entrada de datos.
     y contiene una clave llamada 'estadisticas'. El valor de 'estadisticas' es otro diccionario que
     contiene una clave llamada 'puntos_totales'. El valor de 'puntos_totales'
     :return: una versión ordenada de la matriz de entrada 'arr' usando el algoritmo de clasificación rápida.
            """
            if len(dict) <= 1:
                return dict
            else:
                pivote = dict[0]
                less = [
                    x
                    for x in dict[1:]
                    if x['estadisticas']['puntos_totales'] <= pivote['estadisticas']['puntos_totales']
                ]
                greater = [
                    x
                    for x in dict[1:]
                    if x['estadisticas']['puntos_totales']> pivote['estadisticas']['puntos_totales']
                ]
                return quick_sort(greater) + [pivote] + quick_sort(less)     
            
  
def guardar_posiciones_sqlite():
   # Conecta a la base de datos SQLite
        conn = sqlite3.connect("Posiciones.db")
        cursor = conn.cursor()

        # Crea una tabla si no existe
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS posiciones (
        nombre_posicion TEXT
        )
    '''
        )
        posiciones_validas = ['Base', 'Escolta', 'Alero', 'Ala-Pívot', 'Pívot']
        # Ordena la lista de jugadores con Quick Sort
        try:
            # Inserta los datos en la tabla
            for posicion in posiciones_validas:
                cursor.execute(
                'INSERT INTO posiciones (nombre_posicion) VALUES (?)',(posicion,),
                )
            # Guarda los cambios en la base de datos
            

            print("Lista de posiciones guardada en SQLite.")
        except Exception as e:
            print(f"Error al guardar la lista de posiciones en SQLite: {str(e)}")
        finally:
            # Cierra la conexión a la base de datos
            conn.commit()
            conn.close()
            
def quick_sort_posiciones(dict):
            """
     La función `quick_sort` implementa el algoritmo de clasificación rápida para ordenar una lista de diccionarios según
     el valor de la clave 'puntos_totales' en el diccionario 'estadisticas'.
    
      El parámetro `arr` es una lista de diccionarios. Cada diccionario representa una entrada de datos.
     y contiene una clave llamada 'estadisticas'. El valor de 'estadisticas' es otro diccionario que
     contiene una clave llamada 'puntos_totales'. El valor de 'puntos_totales'
     :return: una versión ordenada de la matriz de entrada 'arr' usando el algoritmo de clasificación rápida.
            """
            if len(dict) <= 1:
                return dict
            else:
                pivote = dict[0]
                less = [
                    x
                    for x in dict[1:]
                    if x['posicion'] <= pivote['posicion']
                ]
                greater = [
                    x
                    for x in dict[1:]
                    if x['posicion']> pivote['posicion']
                ]
                return quick_sort_posiciones(greater) + [pivote] + quick_sort_posiciones(less)             
            
            
equipo = Equipo('Primer_Parcial__1_E.py//dream_team.json')



