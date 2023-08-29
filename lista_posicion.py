from nodo_posicion import nodo_posicion

class lista_posicion:

    def __init__(self):
        self.primero = None
        self.size = 0

    def vacia(self):
        return self.primero == None
    
    def agregar(self,pieza):
        if self.primero is None:
            self.primero = nodo_posicion(posicion = pieza)
            self.size +=1
            return
        
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_posicion(posicion = pieza)
        self.size+=1

    def retornar_posicion(self,fila,columna):
        actual = self.primero
        valor_a_retornar = " "
        while actual != None:
            if (actual.posicion.fila == fila) and (actual.posicion.columna == columna):
                valor_a_retornar =  actual.posicion.color
                break
            actual = actual.siguiente

        return valor_a_retornar
