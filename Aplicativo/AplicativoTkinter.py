from tkinter import *
import tkinter as tk
from Funcoes.Ffuncoes import *
from tkinter import ttk
from PIL import Image, ImageTk


def redimensionar_imagem(event):
    nova_largura = event.width
    nova_altura = event.height
    nova_imagem = imagem_original.resize((nova_largura, nova_altura), Image.ANTIALIAS)
    imagem_tk = ImageTk.PhotoImage(nova_imagem)
    canvas.itemconfig(imagem_id, image=imagem_tk)
    canvas.imagem_tk = imagem_tk  # Para evitar que a imagem seja garbage collected






def centralizar_widget(widget):
    largura_janela = app.winfo_width()
    largura_widget = widget.winfo_width()
    x = (largura_janela - largura_widget) / 2

    widget.place(x=x)


def centralizar_todos_widgets():
    centralizar_widget(botao)
    centralizar_widget(entrada1)
    centralizar_widget(texto1)



app = Tk()

app.title("LDP")
app.geometry("1000x750+610+153")
app.resizable(True, True)
#app.config(bg = 'lightblue')
imagem_original = Image.open("Aplicativo\plane.png")
canvas = tk.Canvas(app, width=1000, height=750)
canvas.pack(fill=tk.BOTH, expand=True)

# Convertendo a imagem original para ImageTk
imagem_tk = ImageTk.PhotoImage(imagem_original)

# Adicionando a imagem ao Canvas
imagem_id = canvas.create_image(0, 0, anchor=tk.NW, image=imagem_tk)

# Ligando o evento de redimensionamento à função de redimensionamento da imagem
app.bind("<Configure>", redimensionar_imagem)


############################################################################################
texto1 = tk.Label(app, text=" Vai ser no crédito ou no débito?",font='TimesNewRoman',background= '#dde', foreground='#000', anchor= tk.W)
texto1.place(relx = 0.2, rely = 0.5)
###############################################
entrada1 = Entry(app, justify=CENTER, font='Impact', border=2,background="#EEE4E8")
entrada1.place(x=0, y=200)  # É necessário posicionar o widget antes de obter suas dimensões
############################################################################################
botao = ttk.Button(app, text="Clique Aqui")
botao.place(x=0, y=100)  # É necessário posicionar o widget antes de obter suas dimensões
############################################################################################















style = ttk.Style()
style.theme_use('xpnative')  # Use 'clam', 'alt', 'default', 'classic', 'vista', ou 'xpnative'.
style.configure("TEntry",
                padding="5 5 5 5",
                foreground="black",
                fieldbackground="white",
               # background="white"
                border = "Red")






app.update_idletasks()  # Atualiza a interface para garantir que as dimensões dos widgets sejam calculadas corretamente

centralizar_todos_widgets()


# Atualizando a posição do botão quando a janela for redimensionada
app.bind("<Configure>", lambda event: centralizar_todos_widgets())































app.mainloop()