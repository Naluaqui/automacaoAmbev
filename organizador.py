import os
import shutil
import time

timeOut = 120

configPath = os.path.join(os.path.dirname(__file__), "config.txt")

with open(configPath, "r") as file:
    linhas = file.readlines()
    initialPath = linhas[0].strip()
    finalPath = linhas[1].strip()

print("Pasta inicial:", initialPath)
print("Pasta final:", finalPath)

initialFolder = os.listdir(initialPath)
finalFolder = os.listdir(finalPath)

while True:
    initialFolder = os.listdir(initialPath)
    if len(initialFolder) == 0:
        time.sleep(60*2)
    else:
        for file in initialFolder:
            local = os.path.join(initialPath, file) 

            for destinoFile in finalFolder:
                folderKey = destinoFile.split('[')[0].strip().lower()
                if folderKey in file.lower():
                    base, ext = os.path.splitext(file)
                    renameFile = "[ASSINADO] " + base + ext

                    filePathMatch = os.path.join(finalPath, destinoFile)
                    filePath = os.path.join(filePathMatch, renameFile)
                    print(f"Movendo {file} para {filePath}")

                    shutil.move(local, filePath)
                    break 

            else:
                base, ext = os.path.splitext(file)
                mkdir = os.path.join(finalPath, base) 
                os.makedirs(mkdir, exist_ok=True)
                renameFile = "[ASSINADO] " + base + ext

                filePath = os.path.join(mkdir, renameFile)
                print(f"Criando pasta {mkdir} e movendo {file} para lá")
                shutil.move(local, filePath)

    initialFolder = os.listdir(initialPath) 