from nodo_tablero import nodo_tablero
import os

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

        for i in range(largo):
            if i>0:
                print('-'*(ancho*2-1))
            
            for j in range(ancho):
                if j+1>0:
                    print('|',end="")
                    print(self.primero.tablero.lista_posiciones.retornar_posicion((i+1),(j+1)),end='')
                    #print("Fila",i,'columna',j,end="")

            print()
    
    def generar_grafica(self):
        f = open('bb.dot','w')
        text = """
        digraph G {
            fontname="Helvetica,Arial,sans-serif"
            node [fontname="Helvetica,Arial,sans-serif"]
            edge [fontname="Helvetica,Arial,sans-serif"]
            a0 [shape=none label=<
            <TABLE border="0" cellspacing="10" cellpadding="10">
        
        """

        ancho = int(self.primero.tablero.ancho)
        largo = int(self.primero.tablero.largo)

        for i in range(largo):
            text += """<TR>"""
            if i>0:
                pass
            for j in range(ancho):
                if j+1>0:
                    valor_color = self.primero.tablero.lista_posiciones.retornar_posicion((i+1),(j+1))
                    if valor_color == "A":
                        text+="""<TD bgcolor="blue">0</TD>"""
                    elif valor_color == "R":
                        text+="""<TD bgcolor="red">0</TD>"""
                    elif valor_color == "V":
                        text+="""<TD bgcolor="green">0</TD>"""
                    elif valor_color == "P":
                        text+="""<TD bgcolor="purple">0</TD>"""
                    elif valor_color == "N":
                        text+="""<TD bgcolor="orange">0</TD>"""
                    elif valor_color == " ":
                        text+= """<TD bgcolor="white">0</TD>"""
            text+="</TR>"
        
        text+="""</TABLE>>];}"""

        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng bb.dot -o Grafica.png')
        print("")
        print("")
        print("")
        print("Grafica terminada!")
