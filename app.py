from lista_tablero import lista_tablero
from tablero import tablero
from lista_posicion import lista_posicion
from posicion import posicion

lista_tablero_temp = lista_tablero()

def crear_tablero():

    lista_posicion_temp = lista_posicion()

    print("")
    print("")
    print("Escriba las filas del tablero:")
    filas = int(input())
    print("Escriba las columnas del tablero:")
    columnas = int(input())
    recorrido = columnas*filas
    condicion = '1'
    contador = 0

    while condicion == '1' and contador<recorrido:
        print("")
        print("Escriba en qué fila desea poner la pieza")
        puesto_fila =  int(input())
        print("Escriba en qué columna desea poner la pieza")
        puesto_columna = int(input())
        print("")
        print("")
        print("Escriba el color que desea agregar")
        print("A para azul")
        print("R para rojo")
        print("V para verde")
        print("P para púrpura")
        print("N para naranja")
        color = input()

        dato = posicion(puesto_fila,puesto_columna,color)
        lista_posicion_temp.agregar(dato)
        print("")
        print("")
        print("Desea poner otra pieza?")
        print("Escriba 1 si desea poner otra pieza")
        print("Escriba 2 si no desea poner otra pieza")
        
        condicion = input()
        contador +=1


    nuevo_tablero = tablero(filas,columnas,lista_posicion_temp)
    lista_tablero_temp.crear_tablero(nuevo_tablero)
    lista_tablero_temp.recorrer_tablero()
    print("Generando grafica...")
    lista_tablero_temp.generar_grafica()

def menu_principal():

    print('')
    print("---------------------BIENVENIDO A GUATEMATEL------------------------")
    print('Menu principal:')
    print('    1. Crear tablero')
    print('    2. Mostrar datos del estudiante')
    print('    3. Salir')

    opcion = input()

    if opcion == '1':
        crear_tablero()
    elif opcion == '2':
        print('')
        print('Datos del estudiante:')
        print('    Carne: 202201211')
        print('    Nombre completo: Jose Leonel Lopez Ajvix')
        print('    Curso: Introduccion a la Programacion y Computacion 2')
        print('    Seccion: D')
        menu_principal()
    elif opcion == '3':
        print("Feliz dia!!")
    else:
        print("Opcion no valida")
        menu_principal()

menu_principal()