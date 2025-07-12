import os
import shutil

initialPath = "C:/Users/analu/OneDrive/Apps/Designer"
finalPath = "C:/finalPath"

initialFolder = os.listdir(initialPath)
finalFolder = os.listdir(finalPath)

while len(initialFolder) != 0:
    for file in initialFolder:
        local = os.path.join(initialPath, file)
        moved = False 

        for destinoFile in finalFolder:
            folder_key = destinoFile.split('[')[0].strip().lower()
            if folder_key in file.lower():
                base, ext = os.path.splitext(file)
                renameFile = "[ASSINADO] " + base + ext

                caminhoMatch = os.path.join(finalPath, destinoFile)
                moveCaminho = os.path.join(caminhoMatch, renameFile)
                print(f"Movendo {file} para {moveCaminho}")

                shutil.move(local, moveCaminho)
                moved = True
                break 

        if not moved:
            base, ext = os.path.splitext(file)
            mkdir = os.path.join(finalPath, base) 
            os.makedirs(mkdir, exist_ok=True)

            moveCaminho = os.path.join(mkdir, file)
            print(f"Criando pasta {mkdir} e movendo {file} para lá")
            shutil.move(local, moveCaminho)

    initialFolder = os.listdir(initialPath) 

print("Feito")   




        