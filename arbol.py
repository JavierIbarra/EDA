import funciones

class Nodo():
    def __init__(self, valor):
        self.padre = None
        self.hijo_Derecho = None
        self.hijo_Izquierdo = None
        self.color = "R"
        self.valor = valor
        self.equilibrio = 0

    def __lt__(self, other):           
        if self.valor < other.valor:
            rst = -1
        elif self.valor > other.valor:
            rst = 1
        else:
            rst = 0
        return rst

class NodeLL():
    def __init__(self,elemento):
        self.key = elemento
        self.next = None
        self.prev = None

class Listaligada():
    def __init__(self, valor):
        self.head = valor
        self.insertados = 1

    def Insertar(self, nuevo):
        nuevo.next = self.head
        if self.head != None:
            self.head.prev = nuevo
        self.head = nuevo
        nuevo.prev = None
        self.insertados += 1

    def Buscar(self, k):
        x = self.head
        while x != None and x.key != k:
            x = x.next
        return x

# AVL
class AVL():
    def __init__(self, raiz):
        self.root = raiz
        self.elementos = 0

    def Insertar(self,nuevo):
        nodo = self.root
        self.elementos+=1
        while True:
             if nuevo.valor < nodo.valor:      # IZQUIERDA
                 nodo.equilibrio -= 1
                 if nodo.hijo_Izquierdo == None:
                     nodo.hijo_Izquierdo = nuevo
                     nuevo.padre = nodo
                     break
                 else:
                     nodo = nodo.hijo_Izquierdo
             else:                                  # DERECHA
                 nodo.equilibrio += 1
                 if nodo.hijo_Derecho == None:
                     nodo.hijo_Derecho = nuevo
                     nuevo.padre = nodo
                     break
                 else:
                     nodo = nodo.hijo_Derecho

        # ------------------------------ Rebalanceo ---------------------------#
        raiz = self.root
        while True:
            if raiz.equilibrio < 0 :
                if raiz.equilibrio == -2:
                    if raiz.hijo_Izquierdo.equilibrio < 0:
                        self.root = funciones.Rotacion_Derecha(raiz)
                        break
                    else:
                        self.root = funciones.Rotacion_Izquierda(raiz.hijo_Izquierdo)
                        funciones.Recorrer(self.root)
                        self.root = funciones.Rotacion_Derecha(raiz)
                        break
                else:
                    raiz = raiz.hijo_Izquierdo
                    if raiz == None:
                        break

            else:
                if raiz.equilibrio == 2:
                    if raiz.hijo_Derecho.equilibrio < 0:
                        self.root = funciones.Rotacion_Derecha(raiz.hijo_Derecho)
                        funciones.Recorrer(self.root)
                        self.root = funciones.Rotacion_Izquierda(raiz)
                        break
                    else:
                        self.root = funciones.Rotacion_Izquierda(raiz)
                        break
                else:
                    raiz = raiz.hijo_Derecho
                    if raiz == None:
                        break

    def Mostrar(self):
        elementos = self.elementos+1
        Lista_Nodos = []
        nodo = self.root
        h = 1
        Lista_Nodos.append(nodo)
        while True:
            try:
                Lista_Nodos.append(nodo.hijo_Izquierdo)
                elementos-=1
            except:
                Lista_Nodos.append(None)
            try:
                Lista_Nodos.append(nodo.hijo_Derecho)
                elementos-=1
            except:
                Lista_Nodos.append(None)


            if elementos < 0:
                break

            nodo = Lista_Nodos[h]
            h+=1

        lista=""
        for nodo in Lista_Nodos:
            if nodo != None:
                lista+=str(nodo.valor)+","
            else:
                lista+=","
        while lista[len(lista)-1]==",":
            lista = lista[0:len(lista)-1]
        print (lista[0:len(lista)])


class Rojo_Negro():
    def __init__(self, raiz):
        self.root = raiz
        self.elementos = 0

    def Insertar(self,nuevo):
        nodo = self.root
        self.elementos+=1
        while True:
             if nuevo.valor < nodo.valor:      # IZQUIERDA
                 nodo.equilibrio -= 1
                 if nodo.hijo_Izquierdo == None:
                     nodo.hijo_Izquierdo = nuevo
                     nuevo.padre = nodo
                     self.root = funciones.Reordenar(nuevo)
                     break
                 else:
                     nodo = nodo.hijo_Izquierdo
             else:                                  # DERECHA
                 nodo.equilibrio += 1
                 if nodo.hijo_Derecho == None:
                     nodo.hijo_Derecho = nuevo
                     nuevo.padre = nodo
                     self.root = funciones.Reordenar(nuevo)
                     break
                 else:
                     nodo = nodo.hijo_Derecho

    def Mostrar(self):
        Lista_Nodos=[]
        nodo = self.root
        elementos = self.elementos+1
        h = 1
        Lista_Nodos.append(nodo)
        while True:
            try:
                Lista_Nodos.append(nodo.hijo_Izquierdo)
                elementos-=1
            except:
                Lista_Nodos.append(None)
            try:
                Lista_Nodos.append(nodo.hijo_Derecho)
                elementos-=1
            except:
                Lista_Nodos.append(None)


            if elementos < 0:
                break

            nodo = Lista_Nodos[h]
            h+=1

        lista=""
        for nodo in Lista_Nodos:
            if nodo != None:
                lista+=str(nodo.valor)+"-"+str(nodo.color)+","
            else:
                lista+=","
        while lista[len(lista)-1]==",":
            lista = lista[0:len(lista)-1]
        print (lista[0:len(lista)])
