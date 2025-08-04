import ctypes
from time import sleep

ctypes.windll.user32.MessageBoxW(0, "Mensagem da notificação", "Título da notificação", 0x40)

print("Script rodou")