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
    count = 0
    for doc in os.listdir(mkdir):
        if doc == renameFile:
            count += 1
            if count == 2:
                os.remove(doc)

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
            configFolder1 = inputimeout(prompt="Quer mudar? Digite o novo caminho ou aguarde para manter:\n>", timeout=5)
            print(f"\n --> Pasta final atual: {finalPath}")
            configFolder2 = inputimeout(prompt="Quer mudar? Digite o novo caminho ou aguarde para manter:\n>", timeout=5)
            
        with open(configPath, "w", encoding="utf-8") as file:
            file.writelines([configFolder1 + "\n", configFolder2 + "\n"])

        return configFolder1.strip(), configFolder2.strip()
    
    except TimeoutOccurred:
        configFolder1 = None
        configFolder2 = None
        print("\n(!!) Tempo esgotado!\n")

ctypes.windll.user32.MessageBoxW(0, "Iniciando Script", "Organizador", 0x40 | 0x1000)
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
        print(f"\n>>> >>> Verificando arquivos na pasta inicial...\nNúmeros de arquivos entrados: {len(initialFolder)}")
        
        configFolderPath()
        time.sleep(5)
            
    for file in initialFolder:

        keyFile = os.path.splitext(file)[0].lower()
        keyFile = re.sub(r'.{2}aditivo', '', keyFile, flags=re.IGNORECASE)
        keyFile = re.sub(r'\b\w{1}\b', '', keyFile, flags=re.IGNORECASE)
        keyFile = re.sub(r'\b\w{2}\b', '', keyFile, flags=re.IGNORECASE)
        keyFile = re.sub(r'cw\w{6}', '', keyFile, flags=re.IGNORECASE)
        keyFile = re.sub(r'\d{2,}', '', keyFile)
        keyFile = re.sub(r" {2,}", '', keyFile)

        if "[" in keyFile:
            keyFile = keyFile.split("[")[0]

        for keyword in ["aditivo", "patrocínio", "patrocinio", "réveillon", "reveillon", "contrato", "réveillon", "pdf", "proposta", "-", "_", "(", ")", ".", "[","]"]:
            if keyword in keyFile:
                keyFile = keyFile.replace(keyword, "").strip()

        keyFile = " ".join(keyFile.split()).strip()

        local = os.path.join(initialPath, file)

        try:
            if len(finalFolder) == 0:
                print(f"\n --> Arquivo encontrado: {file}")
                renameFiles(file, local, keyFile)
                continue

            findFolder = False

            for destinoFile in finalFolder:
                folderKey = destinoFile.lower()
                folderKey = folderKey.replace('[confidencial]', '')
                folderKey = folderKey.split('[')[0].strip()
                folderKey = re.sub(r'\b\w{1}\b', '', folderKey, flags=re.IGNORECASE)
                folderKey = re.sub(r'\b\w{2}\b', '', folderKey, flags=re.IGNORECASE)
                folderKey = re.sub(r'\d{2,}', '', folderKey)
                folderKey = re.sub(r" {2,}", " ", folderKey)

                for keyword in ["confidencial", "patrocínio", "patrocinio", "réveillon", "reveillon", "pdf", "proposta", "-", "_", "(", ")", ".", "[","]"]:
                    if keyword in folderKey:
                        folderKey = folderKey.replace(keyword, "").strip()
                folderKey = " ".join(folderKey.split()).strip()
                
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