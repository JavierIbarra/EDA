import graphviz

# se ingresa el texto de consulta querido
# esta funcion se encarga de leer un archivo y retornar una lista de listas de casos
def leer(texto):   
    while True:
        try:
            nombre = input(texto)
            archivo = open(nombre)
            break
        except IOError:
            print ("\n¡¡¡ Archivo no encontrado !!!\n")

    N_listas = int(archivo.readline())
    i = 0
    listas = []
    while i < N_listas:
        lista = archivo.readline().split(',')   # lista de elementos
        lista = [int(x) for x in lista]
        listas.append(lista)                    # lista de casos a resolver
        i += 1

    return listas

def Mostrar(Arbol, tipo):
    elementos = Arbol.elementos+1
    Lista_Nodos = []
    nodo = Arbol.root
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
            if tipo == "RN":
                lista+=str(nodo.valor)+"-"+str(nodo.color)+","
            else: #AVL
                lista+=str(nodo.valor)+","
        else:
            lista+=","
    
    while lista[len(lista)-1]==",":
        lista = lista[0:len(lista)-1]
    print (lista[0:len(lista)])

def direccion(nodo):    # Indica direccion del nodo con respecto a su padre
    direccion = None
    if nodo.padre != None:
        if nodo.padre.hijo_derecho == nodo:
            direccion = 1
        else:
            direccion = -1
    else:
        direccion = 0
    return direccion

def Nodo_Padre(nodo):
    while nodo.padre != None:
        nodo = nodo.padre
    return nodo

def Rotacion_Izquierda(nodo):
    padre = None
    y = nodo.hijo_Derecho
    nodo.hijo_Derecho = y.hijo_Izquierdo
    if y.hijo_Izquierdo != None:
        y.hijo_Izquierdo.padre = nodo
    y.padre = nodo.padre
    if nodo.padre == None:
        padre = y
    elif nodo == nodo.padre.hijo_Izquierdo:
        nodo.padre.hijo_Izquierdo = y
    else:
        nodo.padre.hijo_Derecho = y
    y.hijo_Izquierdo = nodo
    nodo.padre = y

    if padre != None:
        return padre
    else:
        return Nodo_Padre(nodo)

def Rotacion_Derecha(nodo):
    padre = None
    y = nodo.hijo_Izquierdo
    nodo.hijo_Izquierdo = y.hijo_Derecho
    if y.hijo_Derecho != None:
        y.hijo_Derecho.padre = nodo
    y.padre = nodo.padre
    if nodo.padre == None:
        padre = y
    elif nodo == nodo.padre.hijo_Derecho:
        nodo.padre.hijo_Derecho = y
    else:
        nodo.padre.hijo_Izquierdo = y
    y.hijo_Derecho = nodo
    nodo.padre = y

    if padre != None:
        return padre
    else:
        return Nodo_Padre(nodo)

def LL_Negro(nodo):
    Rotacion_Derecha(nodo.padre.padre)
    ColorAbuelo = nodo.padre.hijo_Derecho.color
    ColorPadre = nodo.padre.color
    nodo.padre.hijo_Derecho.color = ColorPadre
    nodo.padre.color = ColorAbuelo

def LR_Negro(nodo):
    Rotacion_Izquierda(nodo.padre)
    Rotacion_Derecha(nodo.padre)
    ColorAbuelo = nodo.hijo_Derecho.color
    ColorPadre = nodo.color
    nodo.hijo_Derecho.color = ColorPadre
    nodo.color = ColorAbuelo

def RR_Negro(nodo):
    Rotacion_Izquierda(nodo.padre.padre)
    ColorAbuelo = nodo.padre.hijo_Izquierdo.color
    ColorPadre = nodo.padre.color
    nodo.padre.hijo_Izquierdo.color = ColorPadre
    nodo.padre.color = ColorAbuelo

def RL_Negro(nodo):
    Rotacion_Derecha(nodo.padre)
    Rotacion_Izquierda(nodo.padre)
    ColorAbuelo = nodo.hijo_Izquierdo.color
    ColorPadre = nodo.color
    nodo.hijo_Izquierdo.color = ColorPadre
    nodo.color = ColorAbuelo

def Recorrer(arbol):
    if (arbol==None):
        return
    else:
        arbol.equilibrio = Equilibrar(arbol.hijo_Derecho)-Equilibrar(arbol.hijo_Izquierdo)
        Recorrer(arbol.hijo_Izquierdo)
        Recorrer(arbol.hijo_Derecho)

def Equilibrar(nodo):
    altura = 0
    temp = 0

    if nodo == None:
        return 0
    else:
        if nodo.hijo_Izquierdo != None:
            temp = Equilibrar(nodo.hijo_Izquierdo)
            if temp > altura:
                altura = temp
        temp = 0
        if nodo.hijo_Derecho != None:
            temp = Equilibrar(nodo.hijo_Derecho)
            if temp > altura:
                altura = temp
        else:
            altura = 0

    return altura+1

def salida(archivo, lista, tipo, arbol): #tipo de arbol / arbol raiz
    nodo = arbol.nodo(lista[0])    # Crea nuevo nodo
    lista.pop(0)       
    avl = arbol.avl(nodo)       # Crea arbol avl con nodo como raiz
    avl.Insertar(nodo)
    lista_arbol = []        # lista de nodos del arbol
    lista_arbol.append(nodo)

    if tipo == "avl":
        for i in lista:
            nodo = arbol.nodo(i)
            lista_arbol.append(nodo)
            avl.Insertar(nodo)
        
        d = graphviz.Digraph()
        abecedario = list(map(chr,range(65,91)))
        lista_arbol.sort()              
        for i in lista_arbol:
            i.letra = abecedario[0]
            d.node(i.letra,str(i.valor))
            abecedario.pop(0)

        #d.edges(plist)
        d.render()
        

def Reordenar(nodo):
    if nodo.padre == None:
        nodo.color = "N"
        return Nodo_Padre(nodo)
    elif nodo.padre.color == "N":
        return Nodo_Padre(nodo)
    elif nodo.padre.padre.hijo_Derecho == None:        # Nodo NO tiene Tio // Padre es el hijo izquierdo del abuelo
        if nodo.padre.hijo_Derecho == nodo:             # El nodo es el hijo derecho del padre
            LR_Negro(nodo)

        elif nodo.padre.hijo_Izquierdo == nodo:         # El nodo es el hijo izquierdo del padre
            LL_Negro(nodo)

    elif nodo.padre.padre.hijo_Izquierdo == None:        # Nodo NO tiene Tio // Padre es el hijo derecho del abuelo
        if nodo.padre.hijo_Izquierdo == nodo:           # El nodo es el hijo izquierdo del padre
            RL_Negro(nodo)

        elif nodo.padre.hijo_Derecho == nodo:           # El nodo es el hijo derecho del padre
            RR_Negro(nodo)


    else:                           # Si el nodo Tiene Tio
        tio = ["N",None]
        if nodo.padre.padre.hijo_Derecho != nodo.padre:         # El Tio es el hijo derecho del abuelo del nodo
            if nodo.padre.padre.hijo_Derecho.color == "R":      # El Tio es Rojo
                nodo.padre.color = "N"
                nodo.padre.padre.hijo_Derecho.color = "N"
                nodo.padre.padre.color = "R"
                Reordenar(nodo.padre.padre)
                tio[0] = "R"
                tio[1] = 1

        else:                                                   # El Tio es el hijo izquierdo del abuelo del nodo
            if nodo.padre.padre.hijo_Izquierdo.color == "R":    # Tio es Rojo
                nodo.padre.color = "N"                          # padre cambia de color
                nodo.padre.padre.hijo_Izquierdo.color = "N"     # tio cambia de color
                nodo.padre.padre.color = "R"                    # abuelo cambia de color
                Reordenar(nodo.padre.padre)
                tio[0] = "R"
                tio[1] = 0

        if tio[0] == "N":                                       # El Tio es negro
            if tio[1] == 0:                                     # Padre del nodo es el hijo derecho del abuelo
                if nodo.padre.hijo_Izquierdo == nodo:           # El nodo es el hijo izquierdo del padre
                    RL_Negro(nodo)

                elif nodo.padre.hijo_Derecho == nodo:           # El nodo es el hijo derecho del padre
                    RR_Negro(nodo)
            else:                                               # padre del nodo es el hijo izquierdo del abuelo
                if nodo.padre.hijo_Derecho == nodo:             # El nodo es el hijo derecho del padre
                    LR_Negro(nodo)

                elif nodo.padre.hijo_Izquierdo == nodo:         # El nodo es el hijo izquierdo del padre
                    LL_Negro(nodo)

        nodo.padre.color = "N"
        nodo.padre.padre.color = "R"
        Reordenar(nodo.padre.padre)

    return Nodo_Padre(nodo)