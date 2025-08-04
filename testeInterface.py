import tkinter as tk
from tkinter import filedialog, messagebox
import os

def escolher_pasta(entry):
    caminho = filedialog.askdirectory()
    if caminho:
        entry.delete(0, tk.END)
        entry.insert(0, caminho)

def salvar_config():
    pasta_inicial = entry_inicial.get().strip()
    pasta_final = entry_final.get().strip()

    if not os.path.exists(pasta_inicial):
        messagebox.showerror("Erro", "Pasta inicial inválida!")
        return
    if not os.path.exists(pasta_final):
        messagebox.showerror("Erro", "Pasta final inválida!")
        return

    with open(configPath, "w", encoding="utf-8") as file:
        file.writelines([pasta_inicial + "\n", pasta_final + "\n"])

    messagebox.showinfo("Sucesso", "Configurações salvas!")

# Inicialização e leitura do arquivo de config
configPath = os.path.join(os.getenv("APPDATA"), "MeuApp", "config.txt")
if not os.path.exists(configPath):
    os.makedirs(os.path.dirname(configPath), exist_ok=True)
    with open(configPath, "w", encoding="utf-8") as f:
        f.write("PastaInicial\nPastaFinal\n")

with open(configPath, "r", encoding="utf-8") as f:
    lines = f.readlines()
    initialPath = lines[0].strip()
    finalPath = lines[1].strip()

# Interface Tkinter
root = tk.Tk()
root.title("Configurar Pastas")

tk.Label(root, text="Pasta Inicial:").pack()
frame_inicial = tk.Frame(root)
frame_inicial.pack()
entry_inicial = tk.Entry(frame_inicial, width=50)
entry_inicial.pack(side=tk.LEFT, padx=5)
entry_inicial.insert(0, initialPath)
btn_inicial = tk.Button(frame_inicial, text="Selecionar", command=lambda: escolher_pasta(entry_inicial))
btn_inicial.pack(side=tk.LEFT)

tk.Label(root, text="Pasta Final:").pack()
frame_final = tk.Frame(root)
frame_final.pack()
entry_final = tk.Entry(frame_final, width=50)
entry_final.pack(side=tk.LEFT, padx=5)
entry_final.insert(0, finalPath)
btn_final = tk.Button(frame_final, text="Selecionar", command=lambda: escolher_pasta(entry_final))
btn_final.pack(side=tk.LEFT)

btn_salvar = tk.Button(root, text="Salvar Configuração", command=salvar_config)
btn_salvar.pack(pady=20)

root.mainloop()
