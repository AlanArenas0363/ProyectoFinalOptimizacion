import numpy as np
import heapq as hpq #? Se agregó esta nueva librería
#* Instalar 'Better Comments' en Visual Studio Code 

#* Recomendaciones para el usuario
#? Que se agregó/Modificó
#! Variables/Funciones de prueba (Se eliminarán hasta terminar el proyecto)

#? Clase grafo de prueba para el cálculo del problema, puede sufrir cambios o seguir en la version final 
""" class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = np.zeros((vertices, vertices))

    def addLimite(self, src, dest, weight):
        self.graph[src][dest] = weight
        self.graph[dest][src] = weight
"""
def main():
    #? Entradas de texto de los puntos que debe de tomar en cuenta el usuario para resolver el problema
    xInicio = float(input("Punto x inicial: "))
    yInicio = float(input("Punto y inicial: "))
    xFinal = float(input("Punto x final: "))
    xFinal = float(input("Punto y final: "))

    #? Opción de optimización para resolver el problema
    opti = input("Criterio (distancia, tiempo): ")

    if opti == "distancia":
        print("Eligió distancia, se agregará más adelante")
    
    elif opti == "tiempo":
        print("Eligió tiempo, se agregará más adelante")
    
    else:
        print("Criterio inválido")

print("Funciona correctamente") #! NO ELIMINAR HASTA TERMINAR

if __name__ == "__main__":
    main()

#* Revisar Changelog del programa en el README.md de este repositorio
#* Revisar contexto del problema en el README.md de este repositorio