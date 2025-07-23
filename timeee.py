from inputimeout import inputimeout, TimeoutOccurred
import os
configTxt = os.path.join(os.path.dirname(__file__), "arquivo.txt")

try:
    resposta = inputimeout(prompt='Digite seu email: ', timeout=20)
    if resposta != '':
        with open(configTxt, "w", encoding="utf=8") as file:
            file.write(resposta)
except TimeoutOccurred:
    resposta = None
    print("\nTempo esgotado!")

print(f"Você digitou: {resposta}")
