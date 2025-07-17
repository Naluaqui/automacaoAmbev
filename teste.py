import os

# Caminho para o arquivo 'arquivo.txt' (está na mesma pasta do script)
arquivo_path = os.path.join(os.path.dirname(__file__), 'arquivo.txt')

# Tenta abrir e ler o conteúdo do arquivo
try:
    with open(arquivo_path, 'r') as file:
        conteudo = file.read()
        print("Conteúdo do arquivo:")
        print(conteudo)
except FileNotFoundError:
    print(f"O arquivo {arquivo_path} não foi encontrado.")


/projeto
   /dist
      meu_programa.exe
      config.txt
