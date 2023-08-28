from lista_tablero import lista_tablero
from tablero import tablero

lista_tablero_temp = lista_tablero()

def crear_tablero():
    print("")
    print("")
    print("Escriba las filas del tablero:")
    filas = int(input())
    print("Escriba las columnas del tablero:")
    columnas = int(input())
    nuevo_tablero = tablero(filas,columnas,None)
    lista_tablero_temp.crear_tablero(nuevo_tablero)
    lista_tablero_temp.recorrer_tablero()

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
        menu_principal()
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