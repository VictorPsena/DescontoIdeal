from tkinter import*
from tkinter import ttk
import sqlite3
from Ffuncoes import *
import customtkinter
root = customtkinter.CTk()

class Funcs():
    def limpa_tela(self):
        self.ent_bandeira.delete(0, END)
        self.ent_dc.delete(0, END)
        self.ent_par.delete(0, END)
        self.ent_val.delete(0, END)
        self.ent_quant.delete(0, END)
    def conecta_bd(self):
        self.conn = sqlite3.connect('clientes.bd')
        self.cursor = self.conn.cursor(); 
    def desconecta_bd(self):
        self.conn.close(); print('Conectando ao banco de dados')
    def montaTabelas(self):
        self.conecta_bd(); print('Conectando ao banco de dados')
        ### Criar Tabela
        self.cursor.execute("""     
            CREATE TABLE IF NOT EXISTS clients ( 
                cod INTEGER PRIMARY KEY,    
                nome_produto CHAR(50) NOT NULL,
                preço INTEGER(20),
                desconto CHAR(40)
                            
                );
            """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_bd()
    def dc(self):
        self.c = self.ent_dc.get().lower().strip()[0]
        self.lista1 = ['d', 'c']
        try:
            self.lista1.index(self.c)
        except (ValueError, TypeError):
            self.erro = Tk()
            self.erro.geometry("270x100+710+253")
            self.erro.title("ERRO")
            self.erro.resizable(False, False)
            self.texto = Label(self.erro, text="Escolha entre crédito ou débito.",background= '#dde', foreground='#FF6666', anchor= N, font="Impact")
            self.texto.place(x = 10, y =10, width= 250, height= 30)
            self.butao1 = Button(self.erro, text="OK", command= self.erro.destroy,font="Impact", justify=CENTER, foreground="green" )
            self.butao1.place(x = 105, y=50, width=50, height= 30)
            self.erro.mainloop()
        return self.c
    def bandeira(self):
        self.band = self.ent_bandeira.get().lower().strip()[0]
        self.lista = ['e', 'v', 'm', 'h']
        try:
           self.lista.index(self.band)
        except (ValueError, TypeError):
            self.erro = Tk()
            self.erro.geometry("270x100+710+253")
            self.erro.title("ERRO")
            self.erro.resizable(False, False)
            self.texto = Label(self.erro, text="Digite uma bandeira válida. \n  visa, mastercard, elo, hipercard",  
                               background= '#dde', foreground='#FF6666', anchor= N, font="Impact")
            self.texto.place(x = 10, y =10, width= 250, height= 50)
            self.butao2 = Button(self.erro, text="OK", command= self.erro.destroy,font="Impact", justify=CENTER, foreground="green" )
            self.butao2.place(x = 105, y=65, width=50, height= 30)
        

            self.erro.mainloop()
        return self.band    
    def parcelas(self):
        self.p = self.ent_par.get()
        try:
            self.p = int(self.p)
            if self.p > 12 or self.p < 1:
                self.erro = Tk()
                self.erro.geometry("270x100+710+253")
                self.erro.title("ERRO")
                self.erro.resizable(False, False)
                self.texto = Label(self.erro, text="Digite um número de 1 a 12",    
                                   background= '#dde', foreground='#FF6666', anchor= N, font="Impact")
                self.texto.place(x = 10, y =10, width= 250, height= 30)
                self.butao3 = Button(self.erro, text="OK", command= self.erro.destroy,font="Impact", justify=CENTER,  
                       foreground="green" )
                self.butao3.place(x = 105, y=50, width=50, height= 30)
                self.erro.mainloop()
                
        except(ValueError, TypeError):
            self.erro = Tk()
            self.erro.geometry("270x100+710+253")
            self.erro.title("ERRO")
            self.erro.resizable(False, False)
            self.texto = Label(self.erro, text="É um número inteiro." ,background= '#dde',  
                               foreground='#FF6666', anchor= N, font="Impact")
            self.texto.place(x = 10, y =10, width= 250, height= 30)
            self.butao3 = Button(self.erro, text="OK", command= self.erro.destroy,font="Impact", justify=CENTER,  
                       foreground="green" )
            self.butao3.place(x = 105, y=50, width=50, height= 30)
            self.erro.mainloop()

        return self.p   
    def val_produto(self):
        self.v = self.ent_val.get()
        try:
            self.v = float(self.v)
            if  self.v > 50000:
                self.erro = Tk()
                self.erro.geometry("270x100+710+253")
                self.erro.title("ERRO")
                self.erro.resizable(False, False)
                self.texto = Label(self.erro, text="O valor máximo de pruduto é R$50.000",background= '#dde', foreground='#FF6666', anchor= N, font="Impact")
                self.texto.place(x = 10, y =10, width= 250, height= 30)
                self.butao4 = Button(self.erro, text="OK", command= self.erro.destroy,font="Impact", justify=CENTER, foreground="green" )
                self.butao4.place(x = 105, y=50, width=50, height= 30)
            
            elif self.v <= 0:
                self.erro = Tk()
                self.erro.geometry("270x100+710+253")
                self.erro.title("ERRO")
                self.erro.resizable(False, False)
                self.texto = Label(self.erro, text="Seria uma boa comprar de graça.",background= '#dde', foreground='#FF6666', anchor= N, font="Impact")
                self.texto.place(x = 10, y =10, width= 250, height= 30)
                self.butao4 = Button(self.erro, text="OK", command= self.erro.destroy,font="Impact", justify=CENTER, foreground="green" )
                self.butao4.place(x = 105, y=50, width=50, height= 30)
                self.erro.mainloop()

        except(ValueError, TypeError):
                self.erro = Tk()
                self.erro.geometry("270x100+710+253")
                self.erro.title("ERRO")
                self.erro.resizable(False, False)
                self.texto = Label(self.erro, text="Digíte um número, obrigado...",background= '#dde', foreground='#FF6666', anchor= N, font="Impact")
                self.texto.place(x = 10, y =10, width= 250, height= 30)
                self.butao4 = Button(self.erro, text="OK", command= self.erro.destroy,font="Impact", justify=CENTER, foreground="green" )
                self.butao4.place(x = 105, y=50, width=50, height= 30)    
                self.erro.mainloop()
        return self.v
    def widgets_frame_1_1(self):
        self.debcred = self.dc()
        self.bandeiraa = self.bandeira()
        self.parcellas = self.parcelas()
        self.valProduto = self.val_produto()
        # print(self.debcred)
        # print(self.bandeiraa)
        # print(self.parcellas)
        # print(self.valProduto)
        self.taxa = TaxaBandeira(str(self.bandeiraa), self.parcellas, self.debcred)
        # print(self.taxa)
        self.lista = ldp(float(self.valProduto), self.bandeiraa, self.taxa)
        #print(self.lista)

        self.label = customtkinter.CTkLabel(self.frame_1_1,   
                      text= f'Lucro: R${self.lista[0]:.2f} \n Margem de lucro: {self.lista[1]:.2f}% \n Preço Ideal: R${self.lista[2]:.2f} \n  Desconto Máximo: R${self.lista[3]:.2f} \n Lucro mínimo: R${self.lista[4]:.2f} \n Tarifa da maquininha: R${self.lista[5]:.2f} \n Parcelas: R${self.lista[2]/int(self.ent_par.get()):.2f}',    
                      font=('verdana', 20), text_color='#107db2')
        self.label.place(relx=0.02, relheight= 0.96, relwidth= 0.96)

class Aplicativo(Funcs):
    #Coloquei 'Funcs dentro da classe para informar que ela pode utilizar as funções da 'class Funcs'
    # Abre a tela principal do Aplivativo
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets_frame_title()
        self.widgets_frame_1()
        self.lista_frame_2()
        self.montaTabelas()
        root.mainloop()
    def tela(self):
        self.root.title("Calcular o Desconto")
        self.root.configure(background='#1e3743')
        self.root.geometry('800x720')
        self.root.resizable(True, True)
        self.root.maxsize(width=1250, height=1000)
        self.root.minsize(width=1050,height=700)
        self.root._set_appearance_mode('system')   
    def frames(self):
        self.frame_title = customtkinter.CTkFrame(self.root, fg_color='lightgray')
        self.frame_title.place(relx=0.58, rely=0.02, relwidth=0.4, 
                           relheight=0.10)
        ###############################################################################
        self.frame_1 = customtkinter.CTkFrame(self.root, fg_color = 'lightgray',    
                            #highlightbackground='lightblue', highlightthickness=2
                            )
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.55, 
                           relheight=0.46)
        ###############################################################################
        self.frame_1_1 = customtkinter.CTkFrame(self.root, fg_color = 'lightgray',    
                            #highlightbackground='lightblue', highlightthickness=2
                            )
        self.frame_1_1.place(relx=0.58, rely=0.14, relwidth=0.40, 
                           relheight=0.34)
        ###############################################################################
        self.frame_2 = customtkinter.CTkFrame(self.root, fg_color = 'lightgray')
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, 
                           relheight=0.46)
        ###############################################################################        
    def widgets_frame_title(self):
        ###Criação do botão limpar
        self.bt_limpar = customtkinter.CTkButton(self.frame_title, text="Limpar",    
                                font=('verdana', 10, 'bold'), command= self.limpa_tela)
        self.bt_limpar.place(relx= 0.1, rely=0.5, relheight=0.4, relwidth = 0.2)

        ###Criação do botão buscar
        self.bt_config = customtkinter.CTkButton(self.frame_title, text="Config",    
                                font=('verdana', 10, 'bold'))
        self.bt_config.place(relx= 0.32, rely=0.5, relheight=0.4, relwidth = 0.2)

         ###Criação do botão Cadastrar
        self.bt_cadastrar = customtkinter.CTkButton(self.frame_title, text="Cadastrar",  
                               #fg_color='White',   
                                font=('verdana',10, 'bold'))
        self.bt_cadastrar.place(relx= 0.6, rely=0.5, relheight=0.4)

        ### Criação da Label Title
        self.lb_title = Label(self.frame_title, text="Análise de Descontos", bg = 'lightgray',  
                              font=('verdana', 14, 'bold'), fg='#107db2')
        self.lb_title.place(relx=0.1, rely=0.08)    
    def widgets_frame_1(self):

        ### Criação da Label Title
        self.lb_bandeira = customtkinter.CTkLabel(self.frame_1, text="Qual é a bandeira do cartão?",     
                                  font=('verdana', 14), text_color='#107db2')
        self.lb_bandeira.place(relx = 0.03, rely=0.12, relwidth=0.5)

        self.ent_bandeira = customtkinter.CTkEntry(self.frame_1, font=('verdana', 14, 'bold'))
        self.ent_bandeira.place(relx=0.03, rely=0.2, relwidth=0.5, relheight=0.1)
        ###############################################################################
        self.lb_dc = customtkinter.CTkLabel(self.frame_1, text="Vai ser no Crédito ou no Débito?",     
                                  font=('verdana', 14), text_color='#107db2')
        self.lb_dc.place(relx = 0.03, rely=0.32, relwidth=0.5)

        self.ent_dc = customtkinter.CTkEntry(self.frame_1, font=('verdana', 14, 'bold'))
        self.ent_dc.place(relx=0.03, rely=0.4, relwidth=0.5, relheight=0.1)
        ###############################################################################
        self.lb_par = customtkinter.CTkLabel(self.frame_1, text="Quantas Parcelas?",     
                                  font=('verdana', 14), text_color='#107db2')
        self.lb_par.place(relx = 0.03, rely=0.52, relwidth=0.5)

        self.ent_par = customtkinter.CTkEntry(self.frame_1, bg_color = 'White', font=('verdana', 14, 'bold'))
        self.ent_par.place(relx=0.03, rely=0.6, relwidth=0.5, relheight=0.1)
        ###############################################################################
        self.lb_val = customtkinter.CTkLabel(self.frame_1, text="Valor do produto?",     
                                  font=('verdana', 14), text_color='#107db2')
        self.lb_val.place(relx = 0.03, rely=0.72, relwidth=0.5)

        self.ent_val = customtkinter.CTkEntry(self.frame_1, font=('verdana', 14, 'bold'))
        self.ent_val.place(relx=0.03, rely=0.8, relwidth=0.5, relheight=0.1)
        ###############################################################################
        self.lb_quant = customtkinter.CTkLabel(self.frame_1, text="Quantidade do mesmo produto?",     
                                  font=('verdana', 14), text_color='#107db2')
        self.lb_quant.place(relx = 0.55, rely=0.12, relwidth=0.4)

        self.ent_quant = customtkinter.CTkEntry(self.frame_1, font=('verdana', 14, 'bold'))
        self.ent_quant.place(relx=0.55, rely=0.2, relwidth=0.4, relheight=0.1)

        ### Criação do botão enviar 
        self.bt_enviar = customtkinter.CTkButton(self.frame_1, text='Enviar', font=('verdana', 14, 'bold'), command=self.widgets_frame_1_1)
        self.bt_enviar.place(relx= 0.65, rely=0.8, relheight=0.1)         
    def lista_frame_2(self):
        self.ListaCli = ttk.Treeview(self.frame_2, height=3, columns=('clo1', 'clo2', 'clo3','col4'))
        self.ListaCli.heading('#0', text='')
        self.ListaCli.heading('#1', text='Código')
        self.ListaCli.heading('#2', text='Produto')
        self.ListaCli.heading('#3', text='Preço')
        self.ListaCli.heading('#4', text='Desconto')

        self.ListaCli.column('#0', width=1)
        self.ListaCli.column('#1', width=50)
        self.ListaCli.column('#2', width=200)
        self.ListaCli.column('#3', width=125)
        self.ListaCli.column('#4', width=125)

        self.ListaCli.place( relx=0.01, rely=0.1, relheight=0.85, relwidth=0.95)

        self.scrolLista = Scrollbar(self.frame_2, orient='vertical')
        self.ListaCli.configure(yscroll=self.scrolLista.set)
        self.scrolLista.place(relx=0.96, rely=0.1, relwidth=0.02, relheight=0.85)






Aplicativo()














