from time import perf_counter
import arbol
import funciones

#tiempos = []
archivo = funciones.leer("Ingrese nombre del archivo(Arbol AVL): ")

for lista in archivo:
    h = 0
    print (len(lista))
    raiz = arbol.Nodo(lista[h])
    #start = perf_counter()              # Inicio conteo
    Arbol = arbol.AVL(raiz)
    funciones.Mostrar(Arbol,"AVL")
    h+=1

    while h < len(lista):           # Recorrer lista
        elemento = arbol.Nodo(lista[h])
        Arbol.Insertar(elemento)
        funciones.Recorrer(Arbol.root)
        funciones.Mostrar(Arbol,"AVL")
        h+=1
    
    #stop = perf_counter()           # Finaliza conteo

    #tiempos.append([start,stop])       
    
print("\n\n")
#for ti in tiempos:
#    print(ti[1]-ti[0])
