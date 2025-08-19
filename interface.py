import customtkinter  as ctk
import os
from tkinter import filedialog
import subprocess


configPath = os.path.join(os.getenv("APPDATA"), "MeuApp", "config.txt")
ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("Organizador de Arquivos")
app.geometry("600x360")
app.resizable(False, False)

def fileExplorer(entryField):
    directory = filedialog.askdirectory(title="Selecione a pasta")
    if directory:
        entryField.delete(0, "end")
        entryField.insert(0, directory)

def rodarScript():
    subprocess.Popen(["python", "organizador.py"])

def saveConfig():
    initialInput = label1.get().strip()
    finalInput = label2.get().strip()

    with open(configPath, "w", encoding="utf-8") as f:
        f.write(initialInput + "\n")
        f.write(finalInput + "\n")

ctk.CTkButton(app, text="Iniciar Script", command=rodarScript).pack(pady=20)


tittle = ctk.CTkLabel(app, text="Bem-vindo ao Organizador de Arquivos!")
tittle.pack(pady=10)

frame1 = ctk.CTkFrame(app, fg_color="transparent")
frame1.pack(pady=10)

tittleInput1 = ctk.CTkLabel(frame1, text="Pasta Inicial:")
tittleInput1.pack(pady=20, side=ctk.LEFT, padx=10)

label1 = ctk.CTkEntry(frame1, placeholder_text="Digite o caminho da pasta inicial", width=400)
label1.pack(pady=20, side=ctk.LEFT, padx=2)

button1 = ctk.CTkButton(frame1, text="Achar Pasta", command=lambda: fileExplorer(label1))
button1.pack(pady=20, side=ctk.LEFT, padx=10)

frame2 = ctk.CTkFrame(app, fg_color="transparent")
frame2.pack(pady=10)

tittleInput2 = ctk.CTkLabel(frame2, text="Pasta FInal:")
tittleInput2.pack(pady=20, side=ctk.LEFT, padx=10)

label2 = ctk.CTkEntry(frame2, placeholder_text="Digite o caminho da pasta final", width=400)
label2.pack(pady=20, side=ctk.LEFT, padx=6)

button2 = ctk.CTkButton(frame2, text="Achar Pasta", command=lambda: fileExplorer(label2))
button2.pack(pady=20, side=ctk.LEFT, padx=10)

button3 = ctk.CTkButton(app, text="Salvar configurações", command=saveConfig)
button3.pack(pady=20)


app.mainloop()
