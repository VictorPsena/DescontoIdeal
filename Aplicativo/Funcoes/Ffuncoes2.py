from tkinter import*
from tkinter import ttk
import sqlite3
from Ffuncoes import *
import customtkinter
root = customtkinter.CTk()

class Funcs():
    def limpa_tela(self):
        self.ent_codigo.delete(0, END)
        self.ent_bandeira.delete(0, END)
        self.ent_dc.delete(0, END)
        self.ent_par.delete(0, END)
        self.ent_val.delete(0, END)
        self.ent_quant.delete(0, END)
        self.ent_nome.delete(0, END)
    def conecta_bd(self):
        self.conn = sqlite3.connect('clientes.bd')
        self.cursor = self.conn.cursor(); 
    def desconecta_bd(self):
        self.conn.close(); print('Conectando ao banco de dados')
    def montaTabelas(self):
        self.conecta_bd(); print('Conectando ao banco de dados')
        ### Criar Tabela
        self.cursor.execute("""     
            CREATE TABLE IF NOT EXISTS clientes ( 
                cod INTEGER PRIMARY KEY,    
                nome_produto CHAR(50) NOT NULL,
                preço INTEGER(20),
                quantidade CHAR(40)
                            
                );
            """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_bd()
    def variaveis(self):
        self.codigo = self.ent_codigo.get()
        self.entnome = self.ent_nome.get()
        self.desconto = self.ent_par.get()
        self.preço = self.ent_val.get()
        #Variáveis TelaNova
        self.entnome1 = self.ent1_nome.get()
        self.quant1 = self.ent1_quant.get()
        self.preço1 = self.ent1_valor.get()
    def add_produtos(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" INSERT INTO clientes (nome_produto, preço, quantidade)
                            VALUES(?,?,?)""",(self.entnome1, self.preço1, self.quant1))
        self.conn.commit()
        self.desconecta_bd()
        self.select_cadastrar()
    def select_cadastrar(self):
        self.ListaCli.delete(*self.ListaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_produto, preço, quantidade FROM clientes
                                    ORDER BY cod ASC; """) #ASC ordem crescente DES decrescente
        for i in lista:
            self.ListaCli.insert("", END, values =i)
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
        self.taxa = TaxaBandeira(str(self.bandeiraa), self.parcellas, self.debcred)
        self.lista = ldp(float(self.valProduto), self.bandeiraa, self.taxa)
        self.label = customtkinter.CTkLabel(self.frame_1_1,   
                      text= f'Lucro: R${self.lista[0]:.2f} \n Margem de lucro: {self.lista[1]:.2f}% \n Preço Ideal: R${self.lista[2]:.2f} \n  Desconto Máximo: R${self.lista[3]:.2f} \n Lucro mínimo: R${self.lista[4]:.2f} \n Tarifa da maquininha: R${self.lista[5]:.2f} \n Parcelas: R${self.lista[2]/int(self.ent_par.get()):.2f}',    
                      font=('verdana', 20), text_color='#107db2')
        self.label.place(relx=0.02, relheight= 0.96, relwidth= 0.96)
    def DuploClicLista(self, event):
        self.limpa_tela()
        self.ListaCli.selection()

        for n in self.ListaCli.selection():
            col1, col2, col3, col4 = self.ListaCli.item(n, 'values')
            self.ent_codigo.insert(END, col1)
            self.ent_nome.insert(END, col2)
            self.ent_val.insert(END, col3)
            self.ent_par.insert(END, col4)
    def deleta_produto(self):
        self.codigo = self.ent_codigo.get()
        self.entnome = self.ent_nome.get()
        self.desconto = self.ent_par.get()
        self.preço = self.ent_val.get()
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM clientes WHERE cod = ? """, (self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_cadastrar()    
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
        self.select_cadastrar()
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
        self.bt_config = customtkinter.CTkButton(self.frame_title, text="Excluir",    
                                font=('verdana', 10, 'bold'), command= self.deleta_produto)
        self.bt_config.place(relx= 0.32, rely=0.5, relheight=0.4, relwidth = 0.2)

         ###Criação do botão Cadastrar
        self.bt_cadastrar = customtkinter.CTkButton(self.frame_title, text="Cadastrar",  
                               #fg_color='White',   
                                font=('verdana',10, 'bold'), command=self.TelaNova)
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
        self.lb_codigo = customtkinter.CTkLabel(self.frame_1, text="Código",     
                                  font=('verdana', 14), text_color='#107db2')
        self.lb_codigo.place(relx = 0.02, rely=0.01, relwidth=0.1)   
        self.ent_codigo = customtkinter.CTkEntry(self.frame_1, font=('verdana', 14, 'bold'),    
                                                  fg_color="White", text_color="Black")
        self.ent_codigo.place(relx=0.03, rely=0.08, relwidth=0.08, relheight=0.06)
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
        ###############################################################################
        self.lb_nome = customtkinter.CTkLabel(self.frame_1, text="Nome do produto",     
                        font=('verdana', 14), text_color='#107db2')
        self.lb_nome.place(relx = 0.55, rely=0.32, relwidth=0.4)
        self.ent_nome = customtkinter.CTkEntry(self.frame_1, font=('verdana', 14, 'bold'))
        self.ent_nome.place(relx=0.55, rely=0.4, relwidth=0.4, relheight=0.1)
        ### Criação do botão enviar 
        self.bt_enviar = customtkinter.CTkButton(self.frame_1, text='Enviar', font=('verdana', 14, 'bold'), command=self.widgets_frame_1_1)
        self.bt_enviar.place(relx= 0.65, rely=0.8, relheight=0.1)         
    def lista_frame_2(self):
        self.ListaCli = ttk.Treeview(self.frame_2, height=3, columns=('clo1', 'clo2', 'clo3','col4'))
        self.ListaCli.heading('#0', text='')
        self.ListaCli.heading('#1', text='Código')
        self.ListaCli.heading('#2', text='Produto')
        self.ListaCli.heading('#3', text='Preço')
        self.ListaCli.heading('#4', text='Quantidade')

        self.ListaCli.column('#0', width=1)
        self.ListaCli.column('#1', width=50)
        self.ListaCli.column('#2', width=200)
        self.ListaCli.column('#3', width=125)
        self.ListaCli.column('#4', width=125)

        self.ListaCli.place( relx=0.01, rely=0.1, relheight=0.85, relwidth=0.95)

        self.scrolLista = Scrollbar(self.frame_2, orient='vertical')
        self.ListaCli.configure(yscroll=self.scrolLista.set)
        self.scrolLista.place(relx=0.96, rely=0.1, relwidth=0.02, relheight=0.85)
        self.ListaCli.bind("<Double-1>", self.DuploClicLista)      
    def TelaNova(self):
        self.cadastro = customtkinter.CTkToplevel(self.root)
        self.cadastro.title("Cadastro de Produto")
        self.cadastro.configure(background='#1e3743')
        self.cadastro.geometry('600x500')
        self.cadastro.resizable(False, False)
        ###############################################################################
        self.frame_1 = customtkinter.CTkFrame(self.cadastro, fg_color = 'lightgray',    
                            #highlightbackground='lightblue', highlightthickness=2
                            )
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, 
                           relheight=0.94)
        ###############################################################################
        self.lb1_nome = customtkinter.CTkLabel(self.cadastro, text="Nome do produto",     
                        font=('verdana', 14, 'bold'), text_color='#107db2', fg_color='lightgray')
        self.lb1_nome.place(relx = 0.04, rely=0.02, relwidth=0.24)
        self.ent1_nome = Entry(self.cadastro, font=('verdana', 9, 'bold'))
        self.ent1_nome.place(relx=0.04, rely=0.08, relwidth=0.6, relheight=0.05)
        ###############################################################################
        self.lb1_valor = customtkinter.CTkLabel(self.cadastro, text="Valor do produto",     
                        font=('verdana', 14, 'bold'), text_color='#107db2', fg_color='lightgray')
        self.lb1_valor.place(relx = 0.04, rely=0.14, relwidth=0.24)
        self.ent1_valor = Entry(self.cadastro, font=('verdana', 9, 'bold'))
        self.ent1_valor.place(relx=0.04, rely=0.2, relwidth=0.3, relheight=0.05)
        ###############################################################################
        self.lb1_quant = customtkinter.CTkLabel(self.cadastro, text="Quantidade",     
                        font=('verdana', 14, 'bold'), text_color='#107db2', fg_color='lightgray')
        self.lb1_quant.place(relx = 0.04, rely=0.26, relwidth=0.24)
        self.ent1_quant = Entry(self.cadastro, font=('verdana', 9, 'bold'))
        self.ent1_quant.place(relx=0.04, rely=0.32, relwidth=0.3, relheight=0.05)
        
        # Botão Fechar
        self.close_button = customtkinter.CTkButton(self.cadastro, text="Fechar",   
                                                    command=self.cadastro.destroy)
        self.close_button.place(relx = 0.52, rely = 0.8)
        # Botão Cadastrar
        self.close_button = customtkinter.CTkButton(self.cadastro, text="Cadastrar",   
                                                    command=self.add_produtos)
        self.close_button.place(relx = 0.28, rely = 0.8)

        ###############################################################################


Aplicativo()














