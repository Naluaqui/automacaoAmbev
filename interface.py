import customtkinter  as ctk
import os
from tkinter import filedialog
import subprocess
import time


configPath = os.path.join(os.getenv("APPDATA"), "MeuApp", "config.txt")
ctk.set_appearance_mode("dark")



def fileExplorer(entryField):
    directory = filedialog.askdirectory(title="Selecione a pasta")
    if directory:
        entryField.delete(0, "end")
        entryField.insert(0, directory)

def runScript():
    openSecondCtk()
    subprocess.Popen(["python", "organizador.py"])

def saveConfig():
    initialInput = label1.get().strip()
    finalInput = label2.get().strip()

    with open(configPath, "w", encoding="utf-8") as f:
        f.write(initialInput + "\n")
        f.write(finalInput + "\n")

def onSecondCtkClose():
    with open("stop_flag.txt", "w") as f:
        f.write("stop")

    secondCtk.destroy()

def openSecondCtk():
    app.destroy()
    global secondCtk
    secondCtk = ctk.CTkToplevel()

    secondCtk.title("Segunda Tela")
    secondCtk.geometry("650x320")
    #secondCtk.resizable(False, False)

    secondCtk.protocol("WM_DELETE_WINDOW", onSecondCtkClose)

    label = ctk.CTkLabel(secondCtk, text="Essa é a segunda tela!")
    label.pack(pady=20)

    buttonBack = ctk.CTkButton(frame3, text="Salvar configurações", command=lambda: [secondCtk.destroy(), mainApp()])
    buttonBack.pack(pady=20, side=ctk.LEFT, padx=10)

def mainApp():
    global app
    app = ctk.CTk()
    app.title("Organizador de Arquivos")
    app.geometry("650x320")
    app.resizable(False, False)

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

    frame3 = ctk.CTkFrame(app, fg_color="transparent")
    frame3.pack(pady=10)

    button3 = ctk.CTkButton(frame3, text="Salvar configurações", command=saveConfig)
    button3.pack(pady=20, side=ctk.LEFT, padx=10)

    ctk.CTkButton(frame3, text="Iniciar Script", command=runScript).pack(pady=20, side=ctk.LEFT, padx=10)

    app.mainloop()
mainApp()
