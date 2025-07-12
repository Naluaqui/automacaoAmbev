import os
import shutil
import difflib

initialPath = "C:/Users/analu/OneDrive/Área de Trabalho/initialTeste"
finalPath = "C:/finalPath"

initialFolder = os.listdir(initialPath)
finalFolder = os.listdir(finalPath)

while len(initialFolder) != 0:
    moreSimilar = 0
    for file in initialFolder:
        local = os.path.join(initialPath, file)
        for destinoFile in finalFolder:
            folder_key = destinoFile.split('[')[0].strip().lower()
            if folder_key in file.lower():
                base, ext = os.path.splitext(file)
                renameFile = "[ASSINADO] " + base + ext

                caminhoMatch = f"{finalPath}/{destinoFile}"
                moveCaminho = os.path.join(caminhoMatch, renameFile)
                print(f"Movendo {file} para {moveCaminho}")

                shutil.move(local, moveCaminho)
            else:
                continue
print("Feito")
                 




        