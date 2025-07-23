from inputimeout import inputimeout, TimeoutOccurred
import os
configTxt = os.path.join(os.path.dirname(__file__), "arquivo.txt")

try:
    resposta = inputimeout(prompt='Digite o caminho da pasta INICIAL', timeout=20)
    resp = input("teste")
    if resposta != '':
        with open(configTxt, "w", encoding="utf=8") as file:
            file.write(resposta)
except TimeoutOccurred:
    resposta = None
    print("\nTempo esgotado!")

print(f"Você digitou: {resposta}")
