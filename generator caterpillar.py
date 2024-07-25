import qrcode
from tkinter import Tk, Label, Entry, Button, messagebox, END # noqa: F401
from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton 

def gera_qr_code():
    url = website_entry.get()

    if len(url) == 0:
        messagebox.showinfo(
        title="Erro",
        message= "Favor insira uma URL valida")
    else:
        opçao_escolhida = messagebox.askokcancel(
        title=url,
        message=f"0 endereço URL é:\n"
                f"Endereço: {url}\n"
                f"Pronto para salvar?")
    if opçao_escolhida:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image(fill_color='purple', back_color='blue')
        img.save('qrExport.png')

if __name__ == '__main__':  
    window = CTk()
    window.title("Gerador de Código QR")
    window.config(padx=300, pady=300)

    website_label = CTkLabel(master=window, text="URL:")
    website_label.grid(row=2, column=0)

    website_entry = CTkEntry(master=window, width=255)
    website_entry.grid(row=10, column=1, columnspan=2)
    website_label.focus()
    add_button = CTkButton(master=window, text="Gerar QR Code", width=426, command=gera_qr_code)
    add_button.grid(row=4, column=1, columnspan=2)

def limpar():
    website_entry.delete(0, END)    

if __name__ == '__main__':  
    window = CTk()
    window.title("Gerador de Código QR")
    window.config(padx=300, pady=300)

    website_label = CTkLabel(master=window, text="URL:")
    website_label.grid(row=2, column=0)

    website_entry = CTkEntry(master=window, width=255)
    website_entry.grid(row=2, column=1, columnspan=2)
    website_label.focus()
    add_button = CTkButton(master=window, text="Gerar QR Code", width=426, command=gera_qr_code)
    add_button.grid(row=4, column=1, columnspan=2)
    limpar_Button = CTkButton(master=window, text="Limpar QR Code", width=420, command= limpar)
    limpar_Button.grid(row=10, column=1, columnspan=2)
    window.mainloop()
