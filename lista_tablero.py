from nodo_tablero import nodo_tablero

class lista_tablero:

    def __init__(self):
        self.primero = None
        self.size = 0
    
    def vacia(self):
        return self.primero == None
    
    def crear_tablero(self,tablero):
        if self.primero is None:
            self.primero = nodo_tablero(tablero = tablero)
            self.size += 1
            return
        
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_tablero(tablero = tablero)
        self.size+=1

    def recorrer_tablero(self):
        ancho = int(self.primero.tablero.ancho)
        largo = int(self.primero.tablero.largo)

        for ancho in range(ancho):
            for largo in range (largo):
                print(" ",end=" |")
            print("")
