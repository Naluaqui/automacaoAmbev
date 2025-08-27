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
    subprocess.Popen(["python", "uiBase.py"])
    time.sleep(1)
    openSecondCtk()

def saveConfig():

    initialInput = labelInitialFolder.get().strip()
    finalInput = labelFinalFolder.get().strip()

    with open(configPath, "w", encoding="utf-8") as f:
        f.write(initialInput + "\n")
        f.write(finalInput + "\n")

    labelInitialFolder.delete(0, "end")
    labelFinalFolder.delete(0, "end")


def onSecondCtkClose():
    with open("stop_flag.txt", "w") as f:
        f.write("stop")

    secondCtk.destroy()

def showFolder():
    with open(configPath, "r", encoding="utf-8") as file:
        lines = file.readlines()
        initialPath = lines[0].strip()
        finalPath = lines[1].strip()

    initialFolder = os.listdir(initialPath)
    finalFolder = os.listdir(finalPath)

    return initialFolder

def openSecondCtk():
    global secondCtk

    app.destroy()
    secondCtk = ctk.CTkToplevel()

    secondCtk.title("Segunda Tela")
    secondCtk.geometry("650x320")
    secondCtk.resizable(False, False)

    label = ctk.CTkLabel(secondCtk, text=showFolder())
    label.pack(pady=20)

    frameSecondOnTop = ctk.CTkFrame(secondCtk, fg_color="transparent")
    frameSecondOnTop.pack(pady=10)

    tittleSecondInitial = ctk.CTkLabel(frameSecondOnTop, text="Aquivos iniciais encontrados")
    tittleSecondInitial.pack(pady=20, side=ctk.LEFT, padx=10)

    buttonBack = ctk.CTkButton(secondCtk, text="Voltar", command=lambda: [secondCtk.destroy(), mainApp()])
    buttonBack.pack(pady=20, side=ctk.LEFT, padx=10)

    secondCtk.mainloop()

def mainApp():
    global app
    global labelInitialFolder, labelFinalFolder, frameMainBellow

    try:

        app = ctk.CTk()
        app.title("Organizador de Arquivos")
        app.geometry("650x320")
        app.resizable(False, False)

        tittle = ctk.CTkLabel(app, text="Bem-vindo ao Organizador de Arquivos!")
        tittle.pack(pady=10)

        frameMainOnTop = ctk.CTkFrame(app, fg_color="transparent")
        frameMainOnTop.pack(pady=10)

        tittleInput1 = ctk.CTkLabel(frameMainOnTop, text="Pasta Inicial:")
        tittleInput1.pack(pady=20, side=ctk.LEFT, padx=10)

        labelInitialFolder = ctk.CTkEntry(frameMainOnTop, placeholder_text="Digite o caminho da pasta inicial", width=400)
        labelInitialFolder.pack(pady=20, side=ctk.LEFT, padx=2)

        buttonFindFolder1 = ctk.CTkButton(frameMainOnTop, text="Achar Pasta", command=lambda: fileExplorer(labelInitialFolder))
        buttonFindFolder1.pack(pady=20, side=ctk.LEFT, padx=10)

        frameMainAmoung = ctk.CTkFrame(app, fg_color="transparent")
        frameMainAmoung.pack(pady=10)

        tittleInput2 = ctk.CTkLabel(frameMainAmoung, text="Pasta Final:")
        tittleInput2.pack(pady=20, side=ctk.LEFT, padx=10)

        labelFinalFolder = ctk.CTkEntry(frameMainAmoung, placeholder_text="Digite o caminho da pasta final", width=400)
        labelFinalFolder.pack(pady=20, side=ctk.LEFT, padx=6)

        buttonFindFolder2 = ctk.CTkButton(frameMainAmoung, text="Achar Pasta", command=lambda: fileExplorer(labelFinalFolder))
        buttonFindFolder2.pack(pady=20, side=ctk.LEFT, padx=10)

        frameMainBellow = ctk.CTkFrame(app, fg_color="transparent")
        frameMainBellow.pack(pady=10)

        button3 = ctk.CTkButton(frameMainBellow, text="Salvar configurações", command=saveConfig)
        button3.pack(pady=20, side=ctk.LEFT, padx=10)

        ctk.CTkButton(frameMainBellow, text="Iniciar Script", command=runScript).pack(pady=20, side=ctk.LEFT, padx=10)

        app.mainloop()

    except Exception:
        return


mainApp()
