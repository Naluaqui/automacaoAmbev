import os
import shutil
import time
from inputimeout import inputimeout, TimeoutOccurred

configPath = ""

def creatTXT():
    global configPath
    appData = os.getenv("APPDATA")
    folderApp = os.path.join(appData, "MyApp")
    os.makedirs(folderApp, exist_ok=True)
    configPath = os.path.join(folderApp, "config.txt")

    if not os.path.exists(configPath):
        with open(configPath, "w", encoding="utf-8") as f:
            f.write("\n" * 4)

    print(f"'config.txt' criado em: {configPath}")

creatTXT()

def renameFiles(file, local):
    base, ext = os.path.splitext(file)
    mkdir = os.path.join(finalPath, base) 
    os.makedirs(mkdir, exist_ok=True)
    renameFile = "[ASSINADO] " + base + ext
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

    while os.path.exists(initialPath) is False or os.path.exists(finalPath) is False:
        configFolderPath()
        
    initialFolder = os.listdir(initialPath)
    finalFolder = os.listdir(finalPath)

    if len(initialFolder) == 0:
        configFolderPath()
        time.sleep(5)
    
    else:
        for file in initialFolder:
            local = os.path.join(initialPath, file) 

            try:
                for destinoFile in finalFolder:
                    folderKey = destinoFile.split('[')[0].strip().lower()
                    for folderKey in file.lower():
                        renameFiles(file, local)
                        break
            except:
                break

    initialFolder = os.listdir(initialPath)
    time.sleep(5)
