import os
import shutil
import time

def renameFiles(file):
    base, ext = os.path.splitext(file)
    mkdir = os.path.join(finalPath, base) 
    os.makedirs(mkdir, exist_ok=True)
    renameFile = "[ASSINADO] " + base + ext
    newFilePath = os.path.join(mkdir, renameFile)
    shutil.move(local, newFilePath)
    return newFilePath

timeOut = 120

configPath = os.path.join(os.path.dirname(__file__), "config.txt")

with open(configPath, "r", encoding="utf-8") as file:
    linhas = file.readlines()
    initialPath = linhas[0].strip()
    finalPath = linhas[1].strip()

while True:
    initialFolder = os.listdir(initialPath)
    finalFolder = os.listdir(finalPath)

    if len(initialFolder) == 0:
        time.sleep(60*2)
    else:
        for file in initialFolder:
            local = os.path.join(initialPath, file) 

            for destinoFile in finalFolder:
                folderKey = destinoFile.split('[')[0].strip().lower()
                for folderKey in file.lower():
                    renameFiles(file)
                    break

    initialFolder = os.listdir(initialPath)
