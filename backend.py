import numpy as np
import heapq as hpq #? Se agregó esta nueva librería
#* Instalar 'Better Comments' en Visual Studio Code 

#* Recomendaciones para el usuario
#? Que se agregó/Modificó
#! Variables/Funciones de prueba (Se eliminarán hasta terminar el proyecto)

#? Clase grafo de prueba para el cálculo del problema, puede sufrir cambios o seguir en la version final 
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = np.zeros((vertices, vertices))

    def addLimite(self, src, dest, weight):
        self.graph[src][dest] = weight
        self.graph[dest][src] = weight
    
    def metDijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        visitado = [False] * self.V
        pq = [(0, src)]

        while pq:
            d, u = hpq.heappop(pq)
            visitado[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not visitado[v] and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    hpq.heappush(pq, (dist[v], v))
    
        return dist

def main():
    #? Entradas de texto de los puntos que debe de tomar en cuenta el usuario para resolver el problema
    xInicio = float(input("Punto x inicial: "))
    yInicio = float(input("Punto y inicial: "))
    xFinal = float(input("Punto x final: "))
    yFinal = float(input("Punto y final: "))

    #? Opción de optimización para resolver el problema
    opti = input("Criterio (distancia, tiempo): ")

    #? Creación del grafo y añadir los aristas con los pesos correspondientes
    g = Graph(2)
    g.addLimite(0, 1, np.sqrt((xFinal - xInicio)**2 + (yFinal - yInicio)**2))

    #? Ejecutar la función de Dijkstra
    distCorta = g.metDijkstra(0)

    if opti.lower() == "distancia":
        print("La distancia mínimo entre los puntos es: ", distCorta[1], "mts")

    elif opti.lower() == "tiempo":
        tiempo = distCorta[1] / 60 #*Supongamos que va a 60km/hr
        print("El tiempo minimo es de: ", tiempo, "hrs")
    else:
        print("Error")


if __name__ == "__main__":
    main()

#* Revisar Changelog del programa en el README.md de este repositorio
#* Revisar contexto del problema en el README.md de este repositorio