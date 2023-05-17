import tkinter as tk

root = tk.Tk()

class Login():
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()
    
    def tela(self):

        self.root.iconbitmap("AppProject/cadastro_img.ico")

        self.root.title("Login Python")
        self.root.geometry("500x300")
        self.color_background = "#000011"
        self.root.configure(bg=self.color_background)

        self.titulo = tk.Label(self.root, text="Fazer Login", font=("Consolas", 20), background=self.color_background, foreground="White")
        self.titulo.pack(padx=10, pady=10)

        self.email_titulo = tk.Label(self.root, text="E-mail:", font=("Consola", 10), background=self.color_background, foreground="White")
        self.email_titulo.place(relx=0.2, rely=0.25)
        self.email_entry = tk.Entry(self.root, width=30)
        self.email_entry.pack(padx=20, pady=20)

        self.senha_titulo = tk.Label(self.root, text="Senha:", font=("Consolas", 10), background=self.color_background, foreground="White")
        self.senha_titulo.place(relx=0.2, rely=0.42)
        self.senha_entry = tk.Entry(self.root, width=30, show="•")
        self.senha_entry.pack(padx=10, pady=10)

        self.bt_cadastrar = tk.Button(self.root, text="Login", command=None)
        self.bt_cadastrar.pack(padx=20, pady=20)

        self.bt_limpar = tk.Button(self.root, text="Limpar", command=None)
        self.bt_limpar.place(relx=0.72, rely=0.332)

        self.dev = tk.Label(self.root, text="Powered By: Dhenzel_nexxus", font=("Consolas", 12), background=self.color_background, foreground="Green")
        self.dev.pack(padx=10, pady=10)

def main():
    Login()