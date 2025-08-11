import customtkinter

app = customtkinter.CTk()
app.geometry("600x600")

entry = customtkinter.CTkEntry(app, placeholder_text="Adicione o caminho da pasta inicial", width=500)
entry.pack(padx=20, pady=(20, 20), anchor="w")  # Adicione o entry na janela

button = customtkinter.CTkButton(app, text="my button", fg_color="red")
button.pack(padx=20, pady=10)

app.mainloop()
