import customtkinter as ctk
import tkinterDnD as tkdnd
import numpy as np
import heapq as hpq
#* Instalar 'Better Comments' en Visual Studio Code 

#* Recomendaciones para el usuario
#? Que se agregó/Modificó
#! Variables/Funciones de prueba (Se eliminarán hasta terminar el proyecto)

#? Temas para la ventana principal
ctk.set_ctk_parent_class(tkdnd.Tk)
ctk.set_appearance_mode("System")  #* Modos: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("green")  #* Temas: "blue" (standard), "green", "dark-blue"

#? Clase para el grafo para resolver el problema
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

app = ctk.CTk()
app.geometry("440x640")
app.title("Proyecto de Analisis de Algoritmos v0.6 - Programación Loka")

print(type(app), isinstance(app, tkdnd.Tk))

def buttonCallback():
    #? Borra la respuesta anterior para nuevos datos
    txtBxRes.delete(0.0, 'end')

    #? Capturas de información de las entradas de texto
    xInicio = float(entry1.get())
    yInicio = float(entry2.get())
    xFinal = float(entry3.get())
    yFinal = float(entry4.get())

    opti = int(entry5.get())

    #? Creación del grafo y añadir los aristas con los pesos correspondientes
    g = Graph(2)
    g.addLimite(0, 1, np.sqrt((xFinal - xInicio)**2 + (yFinal - yInicio)**2))

    #? Ejecutar la función de Dijkstra
    distCorta = g.metDijkstra(0)

    #? Añadir los resultados al recuadro correspondiente
    if opti == 1:
        #* Si gusta ver la respuesta tanto en la interfaz, como en la terminal. Quite el '#' del print.
        #print("La distancia mínimo entre los puntos es: ", distCorta[1], "mts")
        txtBxRes.insert("0.0", str(distCorta[1]), "mts")

    elif opti == 2:
        tiempo = distCorta[1] / 60 #*Supongamos que va a 60km/hr
        #* Si gusta ver la respuesta tanto en la interfaz, como en la terminal. Quite el '#' del print.
        #print("El tiempo minimo es de: ", tiempo, "hrs")
        txtBxRes.insert("0.0", str(tiempo), "hrs")

    else:
        txtBxRes.insert("0.0", "Errror al mostrar resultado")

#? Borra todos los datos ingresados de todos los texboxes disponibles
def borrarDatos():
    entry1.configure(state="normal")
    entry2.configure(state="normal")
    entry3.configure(state="normal")
    entry4.configure(state="normal")
    entry5.configure(state="normal")

    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')
    entry5.delete(0, 'end')
    txtBxRes.delete(0.0, 'end')

mainFrame = ctk.CTkFrame(master=app)
mainFrame.pack(pady=20, padx=40, fill="both", expand=True)

label1 = ctk.CTkLabel(text="Vehicle Routing Problem (VRP)", master=mainFrame, justify=ctk.LEFT)
label1.pack(pady=10, padx=10)

#* Recuadros de entrada

entry1 = ctk.CTkEntry(master=mainFrame, placeholder_text="Coordenada inicial x")
entry1.pack(pady=10, padx=10)

entry2 = ctk.CTkEntry(master=mainFrame, placeholder_text="Coordenada inicial y")
entry2.pack(pady=10, padx=10)

entry3 = ctk.CTkEntry(master=mainFrame, placeholder_text="Coordenada final x")
entry3.pack(pady=10, padx=10)

entry4 = ctk.CTkEntry(master=mainFrame, placeholder_text="Coordenada final y")
entry4.pack(pady=10, padx=10)

entry5 = ctk.CTkEntry(master=mainFrame, placeholder_text="Método optimo")
entry5.pack(pady=10, padx=10)

btnRes = ctk.CTkButton(text="Calcular", master=mainFrame, command=buttonCallback)
btnRes.pack(pady=10, padx=10)

#? Textboxes

label2 = ctk.CTkLabel(text="Resultados:", master=mainFrame, justify=ctk.RIGHT)
label2.pack(pady=10, padx=10)
txtBxRes = ctk.CTkTextbox(master=mainFrame, height=1) #* Textbox de los resultados
txtBxRes.pack(padx=10)

#? Boton para borrar todo el contenido
btnErrase = ctk.CTkButton(text="Borra el contenido", master=mainFrame, command=borrarDatos)
btnErrase.pack(padx=10, pady=10)

label3 = ctk.CTkLabel(text="Ayuda:", master=mainFrame, justify=ctk.RIGHT)
label3.pack(pady=10, padx=10)
txtBxHelp = ctk.CTkTextbox(master=mainFrame, height=80, width=500) #* Textbox de ayuda al usuario
txtBxHelp.pack(padx=10)
txtBxHelp.insert("0.0", "Al ingresal los datos de 'optimización', ingrese algunas de estas opciones: 'distancia'(1) o 'tiempo'(2)")

app.mainloop()