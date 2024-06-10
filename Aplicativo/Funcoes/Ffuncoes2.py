from tkinter import*

root = Tk()

class Aplicativo():
    # Abre a tela principal do Aplivativo
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        root.mainloop()

    def tela(self):
        self.root.title("Calcular o Desconto")
        self.root.configure(background='#1e3743')
        self.root.geometry('700x500')
        self.root.resizable(True, True)
        self.root.maxsize(width=1250, height=1000)
        self.root.minsize(width=500,height=350)
    
    def frames(self):
        self.frame_1 = Frame(self.root, bd= 2, bg = 'White',    
                            highlightbackground='lightblue', highlightthickness=2)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, 
                           relheight=0.46)
        
        self.frame_2 = Frame(self.root, bd= 2, bg = 'White',    
                            highlightbackground='lightblue', highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, 
                           relheight=0.46)
        


Aplicativo()














