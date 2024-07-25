# import tkinter

# janela = tkinter.Tk()
# janela.geometry("500x300")

# def clique():
#    print("Fazer Login")

# texto = tkinter.TkLabel(janela, text="Fazer Login")
# texto.pack(padx=10, pady=10)

# email = tkinter.TkEntry(janela, placeholder_text="Seu e-mail")
# email.pack(padx=10, pady=10)

# senha = tkinter.TkEntry(janela, placeholder_text="senha", show="*")
# senha.pack(padx=10, pady=10)

# botao = tkinter.TkButton(janela, placeholder_text="login", command=clique)
# botao.pack(padx=10, pady=10)

# janela.mainloop()
import customtkinter

janela = customtkinter.CTk()
janela.geometry("500x300")
janela.config(bg="navy")

def clique():
    print("Fazer Login")

texto = customtkinter.CTkLabel(janela, text="Fazer Login", fg_color="blue")
texto.pack(padx=10, pady=10)

email = customtkinter.CTkEntry(janela, placeholder_text="Seu e-mail", fg_color="red")
email.pack(padx=10, pady=10)

senha = customtkinter.CTkEntry(janela, placeholder_text="Senha", fg_color="purple")
senha.pack(padx=10, pady=10)

nome = customtkinter.CTkEntry(janela, placeholder_text="Nome", fg_color="green")  
nome.pack(padx=10, pady=10)

telefone = customtkinter.CTkEntry(janela, placeholder_text="Telefone", fg_color="black")
telefone.pack(padx=10, pady=10)

botão = customtkinter.CTkButton(janela, text="Login", command=clique ,fg_color="teal")
botão.pack(padx=10, pady=10)

janela.mainloop()