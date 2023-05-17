import tkinter as tk
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

root = tk.Tk()

class Funcs():
    def limpar_tela(self):
        self.email_entry.delete(0, 100)
        self.senha_entry.delete(0, 100)

    def cadastrar(self):
        self.email = self.email_entry.get()
        self.senha = self.senha_entry.get()

        if self.email == "" and self.senha == "":
            self.texto_teste = tk.Label(self.root, text="Por favor, Preencha os campos!", background=self.color_background, foreground="red")
            self.texto_teste.place(relx=0.324, rely=0.5)

        elif self.email == "" and self.senha != "":
            self.texto_teste = tk.Label(self.root, text="Por favor, Informe seu e-mail!", background=self.color_background, foreground="red")
            self.texto_teste.place(relx=0.34, rely=0.5)

        elif self.email != "" and self.senha == "":
            self.texto_teste = tk.Label(self.root, text="Por favor, Defina uma senha !!", background=self.color_background, foreground="red")
            self.texto_teste.place(relx=0.34, rely=0.5)

        else:
            root.destroy()

            self.host = "smtp.gmail.com"
            self.port = "587"
            self.login = "dhenzellimaribeiro@gmail.com"
            self.senha_email = "ziouetlxygyoaydj"

            self.server = smtplib.SMTP(self.host, self.port)

            self.server.ehlo()
            self.server.starttls()

            self.server.login(self.login, self.senha_email)

            self.corpo = """
            Eai Fã de python! 
            Obrigado Por usar meu Aplicativo!
            Se quiser Saber Conhecer mais projetos Meus,
            me siga nas redes sociais.
            Instagram: @dhenzel_nexxus
            XD
            """
            self.email_msg = MIMEMultipart()
            self.email_msg['From'] = self.login
            self.email_msg['To'] = self.email
            self.email_msg['Subject'] = "PYTHON E-mail automatico"
            self.email_msg.attach(MIMEText(self.corpo, 'plain'))

            self.server.sendmail(self.email_msg['From'], self.email_msg['To'], self.email_msg.as_string())

            self.server.quit()

    '''def login(self):
        from login import main
        main()'''
            
            
        
class Cadastro(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()
    
    def tela(self):

        self.root.iconbitmap("AppProject/cadastro_img.ico")

        self.root.title("Cadastro Python")
        self.root.geometry("500x300")
        self.color_background = "#000011"
        self.root.configure(bg=self.color_background)

        self.titulo = tk.Label(self.root, text="Fazer Cadastro", font=("Consolas", 20), background=self.color_background, foreground="White")
        self.titulo.pack(padx=10, pady=10)

        self.email_titulo = tk.Label(self.root, text="E-mail:", font=("Consola", 10), background=self.color_background, foreground="White")
        self.email_titulo.place(relx=0.2, rely=0.25)
        self.email_entry = tk.Entry(self.root, width=30)
        self.email_entry.pack(padx=20, pady=20)

        self.senha_titulo = tk.Label(self.root, text="Senha:", font=("Consolas", 10), background=self.color_background, foreground="White")
        self.senha_titulo.place(relx=0.2, rely=0.42)
        self.senha_entry = tk.Entry(self.root, width=30, show="•")
        self.senha_entry.pack(padx=10, pady=10)

        self.bt_cadastrar = tk.Button(self.root, text="Cadastrar", command=self.cadastrar)
        self.bt_cadastrar.pack(padx=20, pady=20)

        self.bt_limpar = tk.Button(self.root, text="Limpar", command=self.limpar_tela)
        self.bt_limpar.place(relx=0.72, rely=0.332)

        self.dev = tk.Label(self.root, text="Powered By: Dhenzel_nexxus", font=("Consolas", 12), background=self.color_background, foreground="Green")
        self.dev.pack(padx=10, pady=10)

if __name__ == "__main__":
    Cadastro()