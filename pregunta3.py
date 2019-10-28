from time import perf_counter
import arbol
import funciones

#tiempos = []
archivo = funciones.leer("Ingrese nombre del archivo(Arbol RN): ")

for lista in archivo:
    h = 0
    print (len(lista))
    raiz = arbol.Nodo(lista[h])
    raiz.color = "N"
#   start = perf_counter()              # Inicio conteo
    Arbol = arbol.Rojo_Negro(raiz)
    funciones.Mostrar(Arbol,"RN")
    h+=1

    while h < len(lista):           # Recorrer lista
        elemento = arbol.Nodo(lista[h])
        Arbol.Insertar(elemento)
        funciones.Mostrar(Arbol,"RN")
        h+=1

#    stop = perf_counter()           # Finaliza conteo

#    tiempos.append([start,stop])       
    
#print("\n\n")
#for ti in tiempos:
#    print(ti[1]-ti[0])