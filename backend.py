import numpy as np
import heapq #* Se agregó esta nueva librería

#* Para ver los comentarios dinamicamente, instalar 'Better Comments' en Visual Studio Code

#TODO: Programa a realizar acerca del problema del enrutamiento de vehiculo

def main():
    #* Entradas de texto de los puntos que debe de tomar en cuenta el usuario para resolver el problema
    xInicio = float(input("Punto x inicial: "))
    yInicio = float(input("Punto y inicial: "))
    xFinal = float(input("Punto x final: "))
    xFinal = float(input("Punto y final: "))

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