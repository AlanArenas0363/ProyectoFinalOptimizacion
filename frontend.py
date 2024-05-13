import customtkinter as ctk
import tkinterDnD

ctk.set_ctk_parent_class(tkinterDnD.Tk)

ctk.set_appearance_mode("system") # La apariencia se basa en la del sismtema
ctk.set_default_color_theme("dark-blue") # Apariencia de botones

app = ctk.CTk()
app.geometry("400*600")
app.title("Proyecto de Analisis de Algoritmos - Programación Loka")

def buttonCallback():   # Callback del boton de 'Testing'
    print('El botón funciona correctamente')

def creditos():
    cred = ctk.CTk()
    cred.geometry("400*600")
    cred.title("Proyecto de Analisis de Algoritmos - Creditos")

    frameCred = ctk.CTkFrame(master = cred)     # Frame de Creditos
    frameCred.pack(padx=40, pady=20, fill="both", expand=True)

    labelCred = ctk.CTkLabel(text="Creditos", master=frameCred, justify=ctk.LEFT)    # Titulo de Creditos 
    labelCred.pack(pady=10, padx=10)
    
    labelInt1 = ctk.CTkLabel(text="Integrante:", master=frameCred, justify=ctk.LEFT)
    labelInt1.pack(pady=10, padx=10)
    textboxCred1 = ctk.CTkTextbox(master=frameCred, height=1)
    textboxCred1.pack(padx=10)
    labelInt2 = ctk.CTkLabel(text="Integrante:", master=frameCred, justify=ctk.LEFT)
    labelInt2.pack(pady=10, padx=10)
    textboxCred2 = ctk.CTkTextbox(master=frameCred, height=1)
    textboxCred2.pack(padx=10)

    textboxCred1.insert("0.0", "Alan Marcel Arenas Venegas") # Inserta el texto en cada 'textbox' correspondiente
    textboxCred2.insert("0.0", "Jose Armando Equihua Antonio")

    cred.mainloop()

frame1 = ctk.CTkFrame(master = app)     # Frame principal
frame1.pack(padx=40, pady=20, fill="both", expand=True)

label1 = ctk.CTkLabel(text="Vehicle Routing Problem (VRP)", master=frame1, justify=ctk.LEFT)    # Titulo del problema 
label1.pack(pady=10, padx=10)

resBtn = ctk.CTkButton(text="Testing", master=frame1, command=buttonCallback)   # Botón de pruebas #! (ELIMINAR/MODIFICAR DESPUES)
resBtn.pack(pady=10,padx=10)

credBtn = ctk.CTkButton(text="Creditos", master=frame1, command=creditos)   # Botón de Creditos
credBtn.pack(pady=10,padx=10)

app.mainloop()