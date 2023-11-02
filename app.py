from Equipo import *
from jugador import *
from functions import *
#aca importo las bibliotecas que uso en mi modulo app
def menu_opciones(equipo:Equipo):
#defino un menu que va a ser el menu que se muestra en la consola.
    while True:
        print("|=============================================================================================================================|")
        print("|Menú del Dream Team:                                                                                                         |")
        print("|=============================================================================================================================|")
        print("|1. Mostrar la lista de todos los jugadores del Dream Team con el formato: Nombre Jugador - Posición.                         |")
        print("|2. Mostrar jugador por indice con todas sus estadisticas y/o guardarlas  en csv.                                             |")
        print("|3. Buscar jugador por nombre y  y mostrar sus logros, como campeonatos de la NBA, All-Star y Salón de la Fama del Baloncesto |")
        print("|4. Calcular el promedio del total puntos por partido de todo el Dream Team y ordenarlo ascendentemente.                      |")
        print("|5. Buscar jugador por nombre y mostrar si es miembro del Salón de la Fama del Baloncesto.                                    |")
        print("|6. Mostrar el jugador con el mayor numero de rebotes totales de todo el Dream Team.                                          |")
        print("|7. Ordenamiento de la lista de mayor a menor.                                                                                |")
        print("|8. Sumar los datos de los jugadores de robos totales más los bloqueos totales (submenu)                                      |")
        print("|9. Guardar posiciones en el partido.                                                                                          |)")
        print("|10. Saliendo.                                                                                                                 |\n")
        opcion = input("Seleccione una opción: ")
#se valida la opcion del usuario
        if validar_opcion_numero(opcion):
            match opcion:
                case '1':
                    equipo.inicializar_equipo()
                case '2':
                    equipo.mostrar_estadistica_jug_y_guardar_en_csv()
                case '3':
                    lista_de_jugadores_nombres()
                    while True:
                        nombre = input("\nIngrese el nombre del jugador: \n")
                        if validar_jugador_por_nombre(nombre) is True:
                            equipo.buscar_jugador_por_nombre(nombre)
                            break
                case '4':
                    equipo.calcular_promedio_puntos_x_partido()
                case '5':
                    lista_de_jugadores_nombres()
                    while True:
                        nombre_miembro = input("\nIngrese el nombre del jugador para saber si pertenese al salon de la fama de baloncesto: \n")
                        if validar_jugador_por_nombre(nombre_miembro) is True:
                            equipo.mostrar_miembros_del_Salon_de_la_Fama_de_Baloncesto(nombre_miembro)
                            break
                case '6':
                    equipo.calcular_maximo_rebotes_totales()
                case '7':
                    equipo.ordenamiento_mayor_a_menor_guardar_json_y_sqlite()
                case '8':
                    sub_menu_punto_8()
                    option = input("\n Ingrese una opcion del sub menu:")
                    validar_opcion_submenu(option)
                    match option:
                        case '1':
                            mostrar_orden_de_robos_y_bloqueos()
                        case '2':
                            mostrar_jugadores_ordenados_con_porcentaje()
                        case '3':
                            print("Proximamente...\n")   
                case '9':
                    guardar_posiciones_sqlite()
                case '10':
                    print("Saliendo...\n")
                    break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")  