import os
import shutil
import time

initialPath = input("Digite o caminho da pasta inicial: ")
finalPath = "C:/finalPath"

initialFolder = os.listdir(initialPath)
finalFolder = os.listdir(finalPath)

while True: 
    initialFolder = os.listdir(initialPath)
    if len(initialFolder) == 0:
        time.sleep(2 * 60 * 60) 
    else:
        for file in initialFolder:
            local = os.path.join(initialPath, file)
            moved = False 

            for destinoFile in finalFolder:
                folderKey = destinoFile.split('[')[0].strip().lower()
                if folderKey in file.lower():
                    base, ext = os.path.splitext(file)
                    renameFile = "[ASSINADO] " + base + ext

                    filePathMatch = os.path.join(finalPath, destinoFile)
                    filePath = os.path.join(filePathMatch, renameFile)
                    print(f"Movendo {file} para {filePath}")

                    shutil.move(local, filePath)
                    moved = True
                    break 

            if not moved:
                base, ext = os.path.splitext(file)
                mkdir = os.path.join(finalPath, base) 
                os.makedirs(mkdir, exist_ok=True)

                filePath = os.path.join(mkdir, file)
                print(f"Criando pasta {mkdir} e movendo {file} para lá")
                shutil.move(local, filePath)

        initialFolder = os.listdir(initialPath)