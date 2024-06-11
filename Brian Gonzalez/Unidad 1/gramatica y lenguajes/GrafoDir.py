#Código de un grafo dirigirido con 4 elementos
import matplotlib.pyplot as plt

#Creamos un grafo vacío
grafo = {}

#Agregamos vertices al grafo
grafo["A"] = ["B", "C"]
grafo["B"] = ["D"]
grafo["C"] = ["D"]
grafo["D"] = []

#Imprimimos el grafo
print("Grafo: ")
for vertice, adyacente in grafo.items():
    print(f"{vertice} -> {adyacente}")