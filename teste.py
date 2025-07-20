import time
import threading

temp = '3'


def tempo():
    global temp
    global uaaa

    while temp != '5' or uaaa == '':
        time.sleep(10)
        temp = '5'
        print('{temp}\n')
        return temp
    if uaaa == 'config':
        print('Configuração concluída.')
        return uaaa

def jessica():
    global uaaa
    uaaa = input('Digite algo: ')
    return uaaa

threading.Thread(target=tempo).start()
jessica()
print(uaaa)