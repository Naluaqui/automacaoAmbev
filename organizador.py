import os
import shutil
import time
from inputimeout import inputimeout, TimeoutOccurred

configPathTeste = ""

def inicialSettings():
    global configPathTeste
    appData = os.getenv("APPDATA")
    pastaApp = os.path.join(appData, "MeuApp")
    os.makedirs(pastaApp, exist_ok=True)
    configPathTeste = os.path.join(pastaApp, "config.txt")
    if not os.path.exists(configPathTeste):
        with open(configPathTeste, "w", encoding="utf-8") as file:
            file.write("PastaInicial\nPastaFinal\n")

inicialSettings()
configPath = configPathTeste

def renameFiles(file, local, destinoFile):
    mkdir = os.path.join(finalPath, destinoFile) 
    os.makedirs(mkdir, exist_ok=True)
    renameFile = "[ASSINADO] " + file
    newFilePath = os.path.join(mkdir, renameFile)
    shutil.move(local, newFilePath)
    print(f"Movendo arquivo: {file} para {newFilePath}")
    return newFilePath

with open(configPath, "r", encoding="utf-8") as file:
    lines = file.readlines()
    initialPath = lines[0].strip()
    finalPath = lines[1].strip()

def configFolderPath():
    global configPath
    try:


        try:
            with open(configPath, "r", encoding="utf-8") as file:
                lines = file.readlines()
                initialPath = lines[0].strip()
                finalPath = lines[1].strip()
        except:
            initialPath = ""
            finalPath = ""

        if os.path.exists(initialPath) is False or os.path.exists(finalPath) is False:
            print("Pasta INICIAL ou FINAL não encontrada!\n")
            configFolder1 = input("Digite o caminho da pasta INICIAL: ")
            configFolder2 = input("Digite o caminho da pasta FINAL: ")

        else:
            print(f"\nPasta INICIAL: {initialPath}")
            configFolder1 = inputimeout(prompt="Digite o caminho da pasta INICIAL: ", timeout=5)
            print(f"\nPasta FINAL: {finalPath}")
            configFolder2 = inputimeout(prompt="Digite o caminho da pasta FINAL: ", timeout=5)
            
        with open(configPath, "w", encoding="utf-8") as file:
            file.writelines([configFolder1 + "\n", configFolder2 + "\n"])

        return configFolder1.strip(), configFolder2.strip()
    
    except TimeoutOccurred:
        configFolder1 = None
        configFolder2 = None
        print("\nTempo esgotado!")

while True:
    try:
        inicialSettings()
        configPath = configPathTeste
    except:
        print(f"configPathTes = {configPathTeste}")
        print(f"configPath = {configPath}")

    with open(configPath, "r", encoding="utf-8") as file:
                lines = file.readlines()
                initialPath = lines[0].strip()
                finalPath = lines[1].strip()

    while not os.path.exists(initialPath) or not os.path.exists(finalPath):
        configFolderPath()
        
    initialFolder = os.listdir(initialPath)
    finalFolder = os.listdir(finalPath)

    while len(initialFolder) == 0:
        with open(configPath, "r", encoding="utf-8") as file:
                lines = file.readlines()
                initialPath = lines[0].strip()
                
        initialFolder = os.listdir(initialPath)

        print(len(initialFolder))
        
        configFolderPath()
        time.sleep(5)
            
    for file in initialFolder:
        if "aditivo" in file.lower():
            keyFile = file.lower().split("aditivo")[1].strip()
            print(keyFile)
        local = os.path.join(initialPath, file)
        print(local)

        try:
            for destinoFile in finalFolder:
                folderKey = destinoFile.split('[')[0].strip().lower()
                print(folderKey)
                if folderKey in keyFile:
                    print(f"\nArquivo encontrado: {keyFile} -> {folderKey}")
                    renameFiles(file, local, destinoFile)
                    break
        except:
            break

    initialFolder = os.listdir(initialPath)
    time.sleep(5)