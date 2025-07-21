from inputimeout import inputimeout, TimeoutOccurred

try:
    resposta = inputimeout(prompt='Digite seu email: ', timeout=5)
except TimeoutOccurred:
    resposta = None
    print("\nTempo esgotado!")

print(f"Você digitou: {resposta}")