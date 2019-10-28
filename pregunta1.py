from time import perf_counter
import arbol
import funciones

listas = funciones.leer("Ingrese nombre del archivo(lista ligada): ")

print (len(listas))
ListaLigada = None
#start = perf_counter()              # Inicio conteo
for casos in listas:
    nodo = arbol.NodeLL(casos[0])            # creamos elemeto nodo
    ListaLigada = arbol.Listaligada(nodo)  # insertamos nodo a la lista
    casos.pop(0)
    for elemento in casos:
        nodo = arbol.NodeLL(elemento)
        ListaLigada.Insertar(nodo)

    print (ListaLigada.insertados)      # muestra las inserciones en la lista

#stop = perf_counter()

#print ("\n")
#print (start, stop)                 # Finaliza conteo
#print ("Tiempo: ", stop-start)