import os
import shutil
import time
import re
import ctypes
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
    print(f"\n>>> >>> Movendo arquivo: {file} para {newFilePath}")
    print(f"\n**OK** Arquivo movido com sucesso!\n\n{25*"="}\n\n")
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
            ctypes.windll.user32.MessageBoxW(0, "PASTAS NÃO LOCALIZADAS\nCaminhos inválidos, configure novamente!!!\n\nOs caminhos das pastas configurados podem ter sido alterados ou atualizados, ou a permissão de acesso às pastas da rede expirou, exigindo que você faça uma nova autenticação para liberar o acesso.\n\n-> Recomenda-se verificar se as pastas existem nos caminhos configurados e, se forem pastas de rede, confirmar se a autenticação ou conexão foi restabelecida.", "Organizador", 0x10 | 0x1000)
            print(f"{50*"="}\nINICIALIZAÇÃO DO SCRIPT - ORGANIZADOR DE ARQUIVOS\n{50*"="}\n")
            configFolder1 = input("Digite o caminho da pasta INICIAL: ")
            configFolder2 = input("Digite o caminho da pasta FINAL: ")

        else:
            print(f"\n --> Pasta inicial atual: {initialPath}")
            configFolder1 = inputimeout(prompt="Quer mudar? Digite o novo caminho ou aguarde para manter:\n>", timeout=7200)
            print(f"\n --> Pasta final atual: {finalPath}")
            configFolder2 = inputimeout(prompt="Quer mudar? Digite o novo caminho ou aguarde para manter:\n>", timeout=7200)
            
        with open(configPath, "w", encoding="utf-8") as file:
            file.writelines([configFolder1 + "\n", configFolder2 + "\n"])

        return configFolder1.strip(), configFolder2.strip()
    
    except TimeoutOccurred:
        configFolder1 = None
        configFolder2 = None
        print("\n(!!) Tempo esgotado!\n")

while True:
    print("inicializando o script...")
    ctypes.windll.user32.MessageBoxW(0, "Iniciando Script", "Organizador", 0x40 | 0x1000)

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
        print(f"\n>>> >>> Verificando arquivos na pasta inicial...\nNúmeros de arquivos entrados: {len(initialFolder)}")
        
        configFolderPath()
        time.sleep(5)
            
    for file in initialFolder:

        keyFile = os.path.splitext(file)[0].lower()
        match = re.search(r'cw\w{6}', keyFile, re.IGNORECASE)

        if match:
            keyFile = keyFile.replace(match.group(), '')
        if "aditivo" in keyFile:
            keyFile = keyFile.split("aditivo")[1]
        if 'vf' in keyFile:
            keyFile = keyFile.replace('vf', '')
        if 'réveillon' in keyFile:
            keyFile = keyFile.replace('vf', '')
        if "patrocínio" in keyFile:
            keyFile = keyFile.split("patrocínio")[1]
        if "[" in keyFile:
            keyFile = keyFile.split("[")[0]

        keyFile = keyFile.replace("-", " ").replace("_", " ").replace("(", "").replace(")", "").replace("vf", "")
        keyFile = " ".join(keyFile.split()).strip()

        local = os.path.join(initialPath, file)

        try:
            if len(finalFolder) == 0:
                print(f"\n --> Arquivo encontrado: {file}")
                renameFiles(file, local, keyFile)
                continue

            findFolder = False

            for destinoFile in finalFolder:
                folderKey = destinoFile.split('[')[0].strip().lower()

                if "[confidencial]" in folderKey:
                    folderKey = folderKey.replace("[confidencial]", "").strip()
                if "sj" in folderKey:
                    folderKey = folderKey.replace("sj", "").strip()
                if "réveillon" in folderKey:
                    folderKey = folderKey.replace("réveillon", "").strip()
                if "proposta" in folderKey:
                    folderKey = folderKey.replace("proposta", "").strip()
                
                print(f">>> >>> Comparando folderKey='{folderKey}' com keyFile='{keyFile}'")
                time.sleep(1)
                
                if folderKey == '':
                    renameFiles(file, local, keyFile)
                    break

                if folderKey in keyFile:
                    print(f"\n --> Arquivo encontrado: {keyFile} -> {folderKey}")
                    renameFiles(file, local, destinoFile)
                    findFolder = True
                    break 
                else:
                    print("Sem match")

            if not findFolder:
                print(f"\n --> Nenhuma pasta encontrada para o arquivo {file}, criando pasta nova")
                renameFiles(file, local, keyFile)
           
        except Exception as e:
            break

    initialFolder = os.listdir(initialPath)
    time.sleep(5)