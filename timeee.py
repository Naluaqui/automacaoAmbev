from inputimeout import inputimeout, TimeoutOccurred
import os
configTxt = os.path.join(os.path.dirname(__file__), "arquivo.txt")

try:
    resposta = inputimeout(prompt='Digite o caminho da pasta INICIAL', timeout=20)
    resp = inputimeout(prompt='Digite o caminho da pasta FINAL', timeout=20)
    if resposta != '' and resp != '':
        with open(configTxt, "r", encoding="utf-8") as file:
            lines = file.readlines()
            lines[0] = resposta + "\n"
            lines[1] = resp + "\n"
        with open(configTxt, "w", encoding="utf-8") as file:
            file.writelines(lines)
except TimeoutOccurred:
    resposta = None
    resp = None
    print("\nTempo esgotado!")

print(f"Você digitou: {resposta}")
print(f"Você digitou: {resp}")