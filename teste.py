import time
import threading

timeConfig = False

def pausa():
    global timeConfig
    counter = 0
    while counter < 10:
        timeConfig = True
        time.sleep(1)
        counter += 1
        print(counter)
    if counter == 10:
        timeConfig = False
        return timeConfig
        
        

def config():
    global timeConfig
    if timeConfig == True:
        print("Email")
    elif timeConfig == False:
        print("False")
     

threading.Thread(target=pausa).start()
config()




#timeout input

from inputimeout import inputimeout, TimeoutOccurred

try:
    resposta = inputimeout(prompt='Digite seu email: ', timeout=5)
except TimeoutOccurred:
    resposta = None
    print("\nTempo esgotado!")

print(f"Você digitou: {resposta}")
