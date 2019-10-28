from time import perf_counter
import arbol
import funciones

archivo = funciones.leer("Ingrese nombre del archivo: ")

#print (len(archivo))
tiempos = []
ListaLigada = None
for casos in archivo:
    start = perf_counter()              # Inicio conteo
    nodo = arbol.NodeLL(casos[0])            # creamos elemeto nodo
    ListaLigada = arbol.Listaligada(nodo)  # insertamos nodo a la lista
    casos.pop(0)
    for elemento in casos:
        nodo = arbol.NodeLL(elemento)
        ListaLigada.Insertar(nodo)

#    print (ListaLigada.insertados)      # muestra las inserciones en la lista

    stop = perf_counter()
    tiempos.append([start,stop])

print ("\n")

i = 1
for ti in tiempos:
    print("tiempo insercion lista ligada ", i ,": ",ti[1]-ti[0])
    i += 1


tiempos = []

for lista in archivo:
    h = 0
#    print (len(lista))
    raiz = arbol.Nodo(lista[h])
    start = perf_counter()              # Inicio conteo
    Arbol = arbol.AVL(raiz)
#    funciones.Mostrar(Arbol,"AVL")
    h+=1

    while h < len(lista):           # Recorrer lista
        elemento = arbol.Nodo(lista[h])
        Arbol.Insertar(elemento)
        funciones.Recorrer(Arbol.root)
#        funciones.Mostrar(Arbol,"AVL")
        h+=1
    
    stop = perf_counter()           # Finaliza conteo

    tiempos.append([start,stop])       
    
print("\n")
i = 1
for ti in tiempos:
    print("tiempo insercion arbol AVL caso ",i,": ",ti[1]-ti[0])
    i += 1

tiempos = []

for lista in archivo:
    h = 0
#    print (len(lista))
    raiz = arbol.Nodo(lista[h])
    raiz.color = "N"
    start = perf_counter()              # Inicio conteo
    Arbol = arbol.Rojo_Negro(raiz)
#    funciones.Mostrar(Arbol,"RN")
    h+=1

    while h < len(lista):           # Recorrer lista
        elemento = arbol.Nodo(lista[h])
        Arbol.Insertar(elemento)
#        funciones.Mostrar(Arbol,"RN")
        h+=1

    stop = perf_counter()           # Finaliza conteo

    tiempos.append([start,stop])       
    
print("\n")
i = 1
for ti in tiempos:
    print("tiempo insercion arbol rojo-negro ", i ,": ",ti[1]-ti[0])
    i += 1