import tkinter  # noqa: F401
import datetime
import calendar  # noqa: F401
import requests
from tkinter import Label,Frame, Entry,LEFT, HORIZONTAL,NW,FLAT,SOLID,RIDGE, RAISED, Tk, Button, END
from tkinter import ttk
from PIL import ImageTk, Image,ImageOps , ImageDraw  # noqa: F401
from pytube import YouTube
from tkinter.ttk import Progressbar

co0 = "#444466" # Preta
co1 = "#feffff" # branca
co2 = "#6f9fbd" # azul
co3 = "#38576b" # valor

co4 = "#403d3d" # letra
fundo = "#3b3b3b"
janela = Tk()
janela.title('')
janela.geometry('500x300')
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=250)
frame_principal = Frame(janela, width=500, height=110,bg=fundo, pady=5, padx=0, relief="flat",)
frame_principal.grid(row=1, column=0)
frame_quadros = Frame(janela, width=500, height=300,bg=fundo, pady=12, padx=0, relief="flat",)
frame_quadros.grid(row=2, column=0, sticky=NW)
logo = Image.open('images/youtube.png')
logo = logo.resize((50, 50), Image.BILINEAR)
logo = ImageTk.PhotoImage(logo)
l_logo = Label(frame_principal,image=logo, compound=LEFT, bg=fundo, fg="white",font=('Ivy 10 bold'),
anchor="nw", relief=FLAT)
l_logo.place(x=5, y=10)
app_nome = Label(frame_principal, text="YouTube Downloader app", width=32, height=1, padx=0, relief="flat",
anchor="nw", font=('Ivy 15 bold'), bg=fundo, fg=co1)
app_nome.place(x=65, y=15)

def search():

    global img
    url=e_url.get()
    yt=YouTube(url)
    #Title of video
    title=yt.title
    #Number of views of video
    view= yt.views
    #Length of the video
    duration= str(datetime.timedelta(seconds=yt.length))
    #Description of video
    Description=yt.description  # noqa: F841
    #cover of the video
    cover=yt.thumbnail_url
    print(cover)
    img_ = Image.open(requests.get(cover, stream=True).raw)
    img_ = img_.resize((230, 150), Image.ANTIALIAS)

    img_ = ImageTk.PhotoImage(img_)
    img=img_
    l_image['image']=img
    l_title['text']="Titlo : " + str(title)
    l_view['text']="Views : " + str('{:,}'.format(view))
    l_time['text']="Duracao : " + str(duration)

    previousprogress = 0  # noqa: F841
def on_progress(stream, chunk, bytes_remaining):
    global previousprogress
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    liveprogress = (int)(bytes_downloaded / total_size * 100)
    if liveprogress > previousprogress:
        previousprogress = liveprogress
    print(liveprogress)
    bar.place(x=250, y=120)
    bar['value'] = liveprogress
    janela.update_idletasks()
def download():

    url=e_url.get()    # noqa: E999
    yt=YouTube(url)
    yt.register_on_progress_callback(on_progress)
    yt.streams.filter(only_audio=False).first().download()

def limpar():
    e_url.delete(0, END)

l_url = Label(frame_principal, text="Enter URL", height=1,pady=0, padx=0, relief="flat", anchor=NW,font=('Ivy 10 bold'), bg=fundo, fg=co1)
l_url.place(x=10, y=80)
e_url = Entry(frame_principal, width=50, justify='left',relief=SOLID)
e_url.place(x=100, y=80)
b_search = Button(frame_principal, text="Search", width=10, height=1, bg=co2, fg=co1,font=('Ivy 7 bold'),relief=RAISED, overrelief=RIDGE,command = lambda:search())
b_search.place(x=404, y=80)
limpar_url = Button(frame_principal, text="Limpar", width=10, height=1, bg=co2, fg=co1, font=('Arial 10'),relief= RAISED, overrelief=RIDGE,command = lambda:limpar())
limpar_url.place(x=404, y=50)

l_image = Label(frame_quadros, compound=LEFT, bg=fundo, fg="white",font=('Ivy 10 bold'), anchor="nw",relief=FLAT)
l_image.place(x=10, y=10)
l_title = Label(frame_quadros, height=2,pady=0, padx=0,relief="flat",wraplength=225,compound=LEFT,justify='left', anchor=NW, font=('Ivy 10 bold'), bg=fundo, fg=co1)
l_title.place(x=250, y=15)
l_view = Label(frame_quadros, height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 8 bold'), bg=fundo,
fg=co1)

l_view.place(x=250, y=60)
l_time = Label(frame_quadros, height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 8 bold'), bg=fundo,
fg=co1)
l_time.place(x=250, y=85)

down = Image.open('images/download_2.png')
down = down.resize((20, 20))
down = ImageTk.PhotoImage(down)
b_download = Button(frame_quadros, image=down, bg=fundo, fg=co1,font=('airial'), relief=FLAT,
overrelief=RIDGE, command=download)
b_download.place(x=444, y=85)
style = ttk.Style()
style.theme_use('default')
style.configure("black.Horizontal.TProgressbar", background='#00E676')
style.configure("TProgressbar", thickness=6)
bar = Progressbar(frame_quadros, length=190,style='black.Horizontal.TProgressbar')
janela.mainloop()
