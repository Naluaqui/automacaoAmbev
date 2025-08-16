import customtkinter  as ctk
import os
from tkinter import filedialog



ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("Organizador de Arquivos")
app.geometry("600x300")
app.resizable(False, False)

def fileExplorer():
    directory = filedialog.askdirectory(title="Selecione a pasta")
    if directory:
        os.startfile(directory)
    

tittle = ctk.CTkLabel(app, text="Bem-vindo ao Organizador de Arquivos!")
tittle.pack(pady=10)

frame1 = ctk.CTkFrame(app, fg_color="transparent")
frame1.pack(pady=10)

tittleInput1 = ctk.CTkLabel(frame1, text="Pasta Inicial:")
tittleInput1.pack(pady=20, side=ctk.LEFT, padx=10)

label1 = ctk.CTkEntry(frame1, placeholder_text="Digite o caminho da pasta inicial", width=400)
label1.pack(pady=20, side=ctk.LEFT, padx=2)

button1 = ctk.CTkButton(frame1, text="Achar Pasta", command=fileExplorer)
button1.pack(pady=20, side=ctk.LEFT, padx=10)

frame2 = ctk.CTkFrame(app, fg_color="transparent")
frame2.pack(pady=10)

tittleInput2 = ctk.CTkLabel(frame2, text="Pasta FInal:")
tittleInput2.pack(pady=20, side=ctk.LEFT, padx=10)

label2 = ctk.CTkEntry(frame2, placeholder_text="Digite o caminho da pasta final", width=400)
label2.pack(pady=20, side=ctk.LEFT, padx=6)

button2 = ctk.CTkButton(frame2, text="Achar Pasta", command=fileExplorer)
button2.pack(pady=20, side=ctk.LEFT, padx=10)

app.mainloop()

