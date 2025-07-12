import os
import shutil

config_path = os.path.join(os.path.dirname(__file__), "config.txt")

with open(config_path, "r") as file:
    linhas = file.readlines()
    initialPath = linhas[0].strip()
    finalPath = linhas[1].strip()

print("Pasta inicial:", initialPath)
print("Pasta final:", finalPath)

initialFolder = os.listdir(initialPath)
finalFolder = os.listdir(finalPath)

while len(initialFolder) != 0:
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

print("Feito")   




        