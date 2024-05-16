import customtkinter as ctk
import tkinterDnD

ctk.set_ctk_parent_class(tkinterDnD.Tk)

ctk.set_appearance_mode("dark")  #? Modos: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("green")  #? Temas: "blue" (standard), "green", "dark-blue"

app = ctk.CTk()
app.geometry("440x600")
app.title("Proyecto de Analisis de Algoritmos - Programación Loka")

print(type(app), isinstance(app, tkinterDnD.Tk))

def buttonCallback():   #! Callback del boton de 'Calcular'
    print('El botón funciona correctamente')

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

button_1 = ctk.CTkButton(text="Calcular", master=mainFrame, command=buttonCallback)
button_1.pack(pady=10, padx=10)

#* Textboxes

label2 = ctk.CTkLabel(text="Resultados:", master=mainFrame, justify=ctk.RIGHT)
label2.pack(pady=10, padx=10)
txtBxRes = ctk.CTkTextbox(master=mainFrame, height=1) #* Textbox de los resultados
txtBxRes.pack(padx=10)

label3 = ctk.CTkLabel(text="Ayuda:", master=mainFrame, justify=ctk.RIGHT)
label3.pack(pady=10, padx=10)
txtBxHelp = ctk.CTkTextbox(master=mainFrame, height=80, width=500) #* Textbox de ayuda al usuario
txtBxHelp.pack(padx=10)
txtBxHelp.insert("0.0", "Al ingresal los datos de 'optimización', ingrese algunas de estas opciones: 'distancia' o 'tiempo'")

app.mainloop()