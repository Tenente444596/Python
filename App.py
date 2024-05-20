from Usuarios import Usuarios
from tkinter import Frame, Label, Entry, Button, LEFT, RIGHT, END, INSERT,Tk  # noqa: F401
import customtkinter

class Application:
    def __init__(self, master=None):
        self.fonte = ("Franklin Gothic Demi", "14")

        self.container1 = customtkinter.CTkFrame(master=root,fg_color="red")
        self.container1.place(relx=0.5, rely=0.5) 
        self.container1.pack()
        self.container2 = customtkinter.CTkFrame(master=root,fg_color="red")
        self.container2.place(relx=0.5, rely=0.5) 
        self.container2.pack()
        self.container3 = customtkinter.CTkFrame(master=root,fg_color="red")
        self.container3.place(relx=0.5, rely=0.5) 
        self.container3.pack()
        self.container4 = customtkinter.CTkFrame(master=root,fg_color="red")
        self.container4.place(relx=0.5, rely=0.5) 
        self.container4.pack()
        self.container5 = customtkinter.CTkFrame(master=root,fg_color="red")
        self.container5.place(relx=0.5, rely=0.5) 
        self.container5.pack()
        self.container6 = customtkinter.CTkFrame(master=root,fg_color="red")
        self.container6.place(relx=0.5, rely=0.5) 
        self.container6.pack()
        self.container7 = customtkinter.CTkFrame(master=root,fg_color="red")
        self.container7.place(relx=0.5, rely=0.5) 
        self.container7.pack()
        self.container8 = customtkinter.CTkFrame(master=root,fg_color="red")
        self.container8.place(relx=0.5, rely=0.5) 
        self.container8.pack()
        self.container9 = customtkinter.CTkFrame(master=root,fg_color="red")
        self.container9.place(relx=0.5, rely=0.5) 
        self.container9.pack()

        self.titulo = Label(self.container1, text="Colete os dados", 
        font=self.fonte, background= '#00008B',foreground='#008080', width=12)             
        self.titulo["font"] = ("Franklin Gothic Demi", "18", "italic")
        self.titulo.pack ()

        self.lblidusuario = Label(self.container2, text="idUsuario:", 
        font=self.fonte, background= '#00008B',foreground='#008080', width=12)
        self.lblidusuario.pack(side=LEFT)

        self.txtidusuario = Entry(self.container2)
        self.txtidusuario["width"] = 10
        self.txtidusuario["font"] = self.fonte
        self.txtidusuario.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar",
        font=self.fonte, background= '#00008B',foreground='#008080', width=12)
        self.btnBuscar["command"] = self.buscarUsuario
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Nome:",
        font=self.fonte, background= '#00008B',foreground='#008080', width=12)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lbltelefone = Label(self.container4, text="Telefone:",
        font=self.fonte, background= '#00008B',foreground='#008080', width=12)
        self.lbltelefone.pack(side=LEFT)

        self.txttelefone = Entry(self.container4)
        self.txttelefone["width"] = 25
        self.txttelefone["font"] = self.fonte
        self.txttelefone.pack(side=LEFT)

        self.lblemail= Label(self.container5, text="E-mail:",
        font=self.fonte, background= '#00008B',foreground='#008080', width=12)
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(self.container5)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)

        self.lblusuario= Label(self.container6, text="Usuário:",
        font=self.fonte, background= '#00008B',foreground='#008080', width=12)
        self.lblusuario.pack(side=LEFT)

        self.txtusuario = Entry(self.container6)
        self.txtusuario["width"] = 25
        self.txtusuario["font"] = self.fonte
        self.txtusuario.pack(side=LEFT)

        self.lblsenha= Label(self.container7, text="Senha:",
        font=self.fonte, background= '#00008B',foreground='#008080', width=12)
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(self.container7)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha["font"] = self.fonte
        self.txtsenha.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir",
        font=self.fonte, background= '#00008B',foreground='#008080', width=12)
        self.bntInsert["command"] = self.inserirUsuario
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar",
        font=self.fonte, background= '#00008B',foreground='#008080', width=12)
        self.bntAlterar["command"] = self.alterarUsuario
        self.bntAlterar.pack (side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir",
        font=self.fonte, background= '#00008B',foreground='#008080', width=12)
        self.bntExcluir["command"] = self.excluirUsuario
        self.bntExcluir.pack(side=LEFT)

        self.bntLimpar = Button(self.container8, text="Limpar", 
        font=self.fonte, background= '#00008B',foreground='#008080', width=12)
        self.bntLimpar["command"] = self.limparUsuario 
        self.bntLimpar.pack (side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Franklin Gothic Demi", "14", "italic",)
        self.lblmsg.pack()


    def inserirUsuario(self):
        user = Usuarios()

        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.insertUser()

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)


    def alterarUsuario(self):
        user = Usuarios()

        user.idusuario = self.txtidusuario.get()
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.updateUser()

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)

    def excluirUsuario(self):
        user = Usuarios()

        user.idusuario = self.txtidusuario.get()
        self.lblmsg["text"] = user.deleteUser()
        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)


    def buscarUsuario(self):
        user = Usuarios()

        idusuario = self.txtidusuario.get()

        self.lblmsg["text"] = user.selectUser(idusuario)

        self.txtidusuario.delete(0, END)
        self.txtidusuario.insert(INSERT, user.idusuario)
        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.nome)
        self.txttelefone.delete(0, END)
        self.txttelefone.insert(INSERT,user.telefone)
        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, user.email)
        self.txtusuario.delete(0, END)
        self.txtusuario.insert(INSERT, user.usuario)
        self.txtsenha.delete(0, END)
        self.txtsenha.insert(INSERT,user.senha)

    def limparUsuario(self):
        user = Usuarios()    # noqa: F841
        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)
        self.lblmsg["text"] = "Campos limpos com sucesso"

root = Tk()
root.configure(bg='red')
Application(root)
root.mainloop()