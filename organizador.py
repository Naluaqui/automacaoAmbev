import os
import shutil
import time
from inputimeout import inputimeout, TimeoutOccurred

configPath = os.path.join(os.path.dirname(__file__), "config.txt")

def renameFiles(file, local):
    base, ext = os.path.splitext(file)
    mkdir = os.path.join(finalPath, base) 
    os.makedirs(mkdir, exist_ok=True)
    renameFile = "[ASSINADO] " + base + ext
    newFilePath = os.path.join(mkdir, renameFile)
    shutil.move(local, newFilePath)
    return newFilePath

def configFolderPath():
    try:
        configFolder1 = inputimeout(prompt='Digite o caminho da pasta INICIAL: ', timeout=20)
        configFolder2 = inputimeout(prompt='Digite o caminho da pasta FINAL: ', timeout=20)
        if configFolder1 != '' and configFolder2 != '':
            with open(configPath, "r", encoding="utf-8") as file:
                lines = file.readlines()
                lines[0] = configFolder1 + "\n"
                lines[1] = configFolder2 + "\n"
            with open(configPath, "w", encoding="utf-8") as file:
                file.writelines(lines)
    except TimeoutOccurred:
        configFolder1 = None
        configFolder2 = None
        print("\nTempo esgotado!")

    print(f"Você digitou: {configFolder1}")
    print(f"Você digitou: {configFolder2}")

with open(configPath, "r", encoding="utf-8") as file:
    lines = file.readlines()
    initialPath = lines[0].strip()
    finalPath = lines[1].strip()

while True:
    initialFolder = os.listdir(initialPath)
    finalFolder = os.listdir(finalPath)

    if len(initialFolder) == 0:
        configFolderPath()
    else:
        for file in initialFolder:
            local = os.path.join(initialPath, file) 

            for destinoFile in finalFolder:
                folderKey = destinoFile.split('[')[0].strip().lower()
                for folderKey in file.lower():
                    renameFiles(file, local)
                    break

    initialFolder = os.listdir(initialPath)
