from tkinter import*

root = Tk()

class Aplicativo():
    # Abre a tela principal do Aplivativo
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets_frame_title()
        self.widgets_frame_1()
        root.mainloop()

    def tela(self):
        self.root.title("Calcular o Desconto")
        self.root.configure(background='#1e3743')
        self.root.geometry('800x720')
        self.root.resizable(True, True)
        self.root.maxsize(width=1250, height=1000)
        self.root.minsize(width=500,height=600)
    
    def frames(self):
        self.frame_title = Frame(self.root, bd= 2, bg = 'White',    
                            highlightbackground='lightblue', highlightthickness=2)
        self.frame_title.place(relx=0.02, rely=0.02, relwidth=0.96, 
                           relheight=0.10)
        ###############################################################################
        self.frame_1 = Frame(self.root, bd= 2, bg = 'White',    
                            highlightbackground='lightblue', highlightthickness=2)
        self.frame_1.place(relx=0.02, rely=0.14, relwidth=0.47, 
                           relheight=0.34)
        ###############################################################################
        self.frame_1_1 = Frame(self.root, bd= 2, bg = 'White',    
                            highlightbackground='lightblue', highlightthickness=2)
        self.frame_1_1.place(relx=0.51, rely=0.14, relwidth=0.47, 
                           relheight=0.34)
        ###############################################################################
        self.frame_2 = Frame(self.root, bd= 2, bg = 'White',    
                            highlightbackground='lightblue', highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, 
                           relheight=0.46)
        ###############################################################################
        
    def widgets_frame_title(self):
        ###Criação do botão limpar
        self.bt_limpar = Button(self.frame_title, text="Limpar", bd=2, bg='#107db2', fg='White',    
                                font=('verdana', 8, 'bold'))
        self.bt_limpar.place(relx= 0.4, rely=0.5, relheight=0.4)
        ###Criação do botão buscar
        self.bt_config = Button(self.frame_title, text="Config", bd=2, bg='#107db3', fg='White',    
                                font=('verdana', 8, 'bold'))
        self.bt_config.place(relx= 0.5, rely=0.5, relheight=0.4)
         ###Criação do botão Cadastrar
        self.bt_cadastrar = Button(self.frame_title, text="Cadastrar", bd=2, bg='#107db4',  
                                fg='White', font=('verdana', 8, 'bold'))
        self.bt_cadastrar.place(relx= 0.6, rely=0.5, relheight=0.4)

        ### Criação da Label Title
        self.lb_title = Label(self.frame_title, text="Análise de Descontos", bg = 'White', font=('verdana', 10, 'bold'), fg='#107db2')
        self.lb_title.place(relx=0.42, rely=0.1)

    
    def widgets_frame_1(self):
        ### Criação da Label Title
        self.lb_bandeira = Label(self.frame_1, text="Qual é a bandeira do cartão?",     
                                 bg = 'White', font=('verdana', 9), fg='#107db2')
        self.lb_bandeira.place(relx = 0.05, rely=0.08, relwidth=0.5)

        self.ent_bandeira = Entry(self.frame_1, bg = 'White', font=('verdana', 8, 'bold'), fg='#107db2')
        self.ent_bandeira.place(relx=0.05, rely=0.2, relwidth=0.5, relheight=0.1)

Aplicativo()














