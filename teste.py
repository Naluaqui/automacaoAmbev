import os

# Caminho do AppData\Roaming
appData = os.getenv("APPDATA")

# Caminho da pasta do seu app dentro do AppData
pastaApp = os.path.join(appData, "MeuApp")

# Garante que a pasta exista
os.makedirs(pastaApp, exist_ok=True)

# Caminho completo do arquivo config.txt
configPath = os.path.join(pastaApp, "config.txt")

# Verifica se o arquivo existe. Se não existir, cria um vazio
if not os.path.exists(configPath):
    with open(configPath, "w", encoding="utf-8") as file:
        file.write("")  # Ou escreva conteúdo padrão, se quiser

print(f"'config.txt' pronto em: {configPath}")