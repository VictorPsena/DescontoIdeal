from tkinter import*
from tkinter import ttk
import sqlite3
from Ffuncoes import*

root = Tk()
class Teste():
    def teste(self):
        self.soma = 1
     # def add_cliente(self):
    #     self.codigo = self.ent_bandeira.get()
    #     self.nome = self.ent_db.get()
    #     self.telefone = self.ent_par.get()
    #     self.cidade = self.ent_val.get()
    #     self.quant = self.ent_quant.get()

    #     self.cursor.execute(""" INSERT INTO clientes (nome_clientes, telefone, cidade)
    #                         VALUES (?, ?, ?) """, (self.bandeira, self.db, self.par))
    #     self.conn.commit()
    #     self.desconecta_bd()
    #     self.select_lista()
    #     self.limpa_tela()

    # def select_lista(self):
    #     self.ListaCli.delete(*self.ListaCli.get_children())
    #     self.conecta_bd()
    #     lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes    
    #         ORDER BY nome_clientes ASC; """)
    #     for i in lista:
    #         self.ListaCli.insert("", END, values=i)
    #     self.desconecta_bd()

class Funcs():
    def limpa_tela(self):
        self.ent_bandeira.delete(0, END)
        self.ent_dc.delete(0, END)
        self.ent_par.delete(0, END)
        self.ent_val.delete(0, END)
        self.ent_quant.delete(0, END)
    def conecta_bd(self):
        self.conn = sqlite3.connect('clientes.bd')
        self.cursor = self.conn.cursor(); print('Conectando ao banco de dados')
    def desconecta_bd(self):
        self.conn.close(); print('Conectando ao banco de dados')
    def montaTabelas(self):
        self.conecta_bd(); print('Desconectando ao banco de dados')
        ### Criar Tabela
        self.cursor.execute("""     
            CREATE TABLE IF NOT EXISTS clients ( 
                cod INTEGER PRIMARY KEY,    
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
                            
                );
            """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_bd()
    def bandeira(self):
        band = self.ent_bandeira.get().lower().strip()
        lista = ['elo', 'visa', 'mastercard', 'hipercard']
        try:
            lista.index(band)
        except (ValueError, TypeError):
            erro = Tk()
            erro.geometry("270x100+710+253")
            erro.title("ERRO")
            erro.resizable(False, False)
            texto = Label(erro, text="Digite uma bandeira válida. \n visa, mastercard, elo, hipercard",background= '#dde', foreground='#FF6666', anchor= N, font="Impact")
            texto.place(x = 10, y =10, width= 250, height= 50)
            Button(erro, text="OK", command= erro.destroy,font="Impact", justify=CENTER, foreground="green" ).place(x = 105, y=65, width=50, height= 30)
        

            erro.mainloop()
        return band
    def dc(self):
        c = self.ent_dc.get().lower().strip()[0]
        lista1 = ['d', 'c']
        try:
            lista1.index(c)
        except (ValueError, TypeError):
            erro = Tk()
            erro.geometry("270x100+710+253")
            erro.title("ERRO")
            erro.resizable(False, False)
            texto = Label(erro, text="Escolha entre crédito ou débito.",background= '#dde', foreground='#FF6666', anchor= N, font="Impact")
            texto.place(x = 10, y =10, width= 250, height= 30)
            Button(erro, text="OK", command= erro.destroy,font="Impact", justify=CENTER, foreground="green" ).place(x = 105, y=50, width=50, height= 30)
        

            erro.mainloop()
        return c
    def parcelas(self):
        p = self.ent_par.get()
        try:
            p = int(p)
            if p > 12 or p < 1:
                erro = Tk()
                erro.geometry("270x100+710+253")
                erro.title("ERRO")
                erro.resizable(False, False)
                texto = Label(erro, text="Digite um número de 1 a 12",background= '#dde',   
                              foreground='#FF6666', anchor= N, font="Impact")
                texto.place(x = 10, y =10, width= 250, height= 30)
                Button(erro, text="OK", command= erro.destroy,font="Impact", justify=CENTER,    
                       foreground="green" ).place(x = 105, y=50, width=50, height= 30)
            

                erro.mainloop()

        except(ValueError, TypeError):
            erro = Tk()
            erro.geometry("270x100+710+253")
            erro.title("ERRO")
            erro.resizable(False, False)
            texto = Label(erro, text="É um número inteiro." ,   
                          background= '#dde', foreground='#FF6666', anchor= N, font="Impact")
            texto.place(x = 10, y =10, width= 250, height= 30)
            Button(erro, text="OK", command= erro.destroy,font="Impact",    
                   justify=CENTER, foreground="green" ).place(x = 105, y=50, width=50, height= 30)
        

            erro.mainloop()
        return p   
    def val_produto(self):
        v = self.ent_val.get()
        try:
            v = float(v)
            if  v > 50000:
                erro = Tk()
                erro.geometry("270x100+710+253")
                erro.title("ERRO")
                erro.resizable(False, False)
                texto = Label(erro, text="O valor máximo de pruduto é R$50.000",    
                              background= '#dde', foreground='#FF6666', anchor= N, font="Impact")
                texto.place(x = 10, y =10, width= 250, height= 30)
                Button(erro, text="OK", command= erro.destroy,font="Impact", justify=CENTER,    
                       foreground="green" ).place(x = 105, y=50, width=50, height= 30)
            
            elif v <= 0:
                erro = Tk()
                erro.geometry("270x100+710+253")
                erro.title("ERRO")
                erro.resizable(False, False)
                texto = Label(erro, text="Seria uma boa comprar de graça.", 
                              background= '#dde', foreground='#FF6666', anchor= N, font="Impact")
                texto.place(x = 10, y =10, width= 250, height= 30)
                Button(erro, text="OK", command= erro.destroy,font="Impact", justify=CENTER,    
                       foreground="green" ).place(x = 105, y=50, width=50, height= 30)


            

                erro.mainloop()
        except(ValueError, TypeError):
                erro = Tk()
                erro.geometry("270x100+710+253")
                erro.title("ERRO")
                erro.resizable(False, False)
                texto = Label(erro, text="Digíte um número, obrigado...",background= '#dde',    
                              foreground='#FF6666', anchor= N, font="Impact")
                texto.place(x = 10, y =10, width= 250, height= 30)
                Button(erro, text="OK", command= erro.destroy,font="Impact", justify=CENTER,    
                       foreground="green" ).place(x = 105, y=50, width=50, height= 30)    

                
                erro.mainloop()
        #return v
    


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
        self.bandeira()
        self.dc()
        #self.select_lista()
        root.mainloop()
    def tela(self):
        self.root.title("Calcular o Desconto")
        self.root.configure(background='#1e3743')
        self.root.geometry('800x720')
        self.root.resizable(True, True)
        self.root.maxsize(width=1250, height=1000)
        self.root.minsize(width=1050,height=700)   
    def frames(self):
        self.frame_title = Frame(self.root, bd= 2, bg = 'White',    
                            highlightbackground='lightblue', highlightthickness=2)
        self.frame_title.place(relx=0.58, rely=0.02, relwidth=0.4, 
                           relheight=0.10)
        ###############################################################################
        self.frame_1 = Frame(self.root, bd= 2, bg = 'White',    
                            highlightbackground='lightblue', highlightthickness=2)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.55, 
                           relheight=0.46)
        ###############################################################################
        self.frame_1_1 = Frame(self.root, bd= 2, bg = 'White',    
                            highlightbackground='lightblue', highlightthickness=2)
        self.frame_1_1.place(relx=0.58, rely=0.14, relwidth=0.40, 
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
                                font=('verdana', 8, 'bold'), command= self.limpa_tela)
        self.bt_limpar.place(relx= 0.1, rely=0.5, relheight=0.4)

        ###Criação do botão buscar
        self.bt_config = Button(self.frame_title, text="Config", bd=2, bg='#107db3', fg='White',    
                                font=('verdana', 8, 'bold'))
        self.bt_config.place(relx= 0.24, rely=0.5, relheight=0.4)

         ###Criação do botão Cadastrar
        self.bt_cadastrar = Button(self.frame_title, text="Cadastrar", bd=2, bg='#107db4',  
                                fg='White', font=('verdana', 8, 'bold'))
        self.bt_cadastrar.place(relx= 0.8, rely=0.5, relheight=0.4)

        ### Criação da Label Title
        self.lb_title = Label(self.frame_title, text="Análise de Descontos", bg = 'White',  
                              font=('verdana', 10, 'bold'), fg='#107db2')
        self.lb_title.place(relx=0.1, rely=0.1)    
    def widgets_frame_1(self):

        ### Criação da Label Title
        self.lb_bandeira = Label(self.frame_1, text="Qual é a bandeira do cartão?",     
                                 bg = 'White', font=('verdana', 9), fg='#107db2')
        self.lb_bandeira.place(relx = 0.03, rely=0.08, relwidth=0.5)

        self.ent_bandeira = Entry(self.frame_1, bg = 'White', font=('verdana', 8, 'bold'), fg='#107db2')
        self.ent_bandeira.place(relx=0.03, rely=0.2, relwidth=0.5, relheight=0.1)
        ###############################################################################
        self.lb_dc = Label(self.frame_1, text="Vai ser no Crédito ou no Débito?",     
                                 bg = 'White', font=('verdana', 9), fg='#107db2')
        self.lb_dc.place(relx = 0.03, rely=0.3, relwidth=0.5)

        self.ent_dc = Entry(self.frame_1, bg = 'White', font=('verdana', 8, 'bold'), fg='#107db2')
        self.ent_dc.place(relx=0.03, rely=0.4, relwidth=0.5, relheight=0.1)
        ###############################################################################
        self.lb_par = Label(self.frame_1, text="Quantas Parcelas?",     
                                 bg = 'White', font=('verdana', 9), fg='#107db2')
        self.lb_par.place(relx = 0.03, rely=0.5, relwidth=0.5)

        self.ent_par = Entry(self.frame_1, bg = 'White', font=('verdana', 8, 'bold'), fg='#107db2')
        self.ent_par.place(relx=0.03, rely=0.6, relwidth=0.5, relheight=0.1)
        ###############################################################################
        self.lb_val = Label(self.frame_1, text="Valor do produto?",     
                                 bg = 'White', font=('verdana', 9), fg='#107db2')
        self.lb_val.place(relx = 0.03, rely=0.7, relwidth=0.5)

        self.ent_val = Entry(self.frame_1, bg = 'White', font=('verdana', 8, 'bold'), fg='#107db2')
        self.ent_val.place(relx=0.03, rely=0.8, relwidth=0.5, relheight=0.1)
        ###############################################################################
        self.lb_quant = Label(self.frame_1, text="Quantidade do mesmo produto?",     
                                 bg = 'White', font=('verdana', 9), fg='#107db2')
        self.lb_quant.place(relx = 0.5, rely=0.08, relwidth=0.5)

        self.ent_quant = Entry(self.frame_1, bg = 'White', font=('verdana', 8, 'bold'), fg='#107db2')
        self.ent_quant.place(relx=0.55, rely=0.2, relwidth=0.4, relheight=0.1)

        ### Criação do botão enviar
        self.bt_enviar = Button(self.frame_1, text='Enviar', bd=2, bg='#107db4',  
                                fg='White', font=('verdana', 8, 'bold'))
        self.bt_enviar.place(relx= 0.85, rely=0.8, relheight=0.1)
    def lista_frame_2(self):
        self.ListaCli = ttk.Treeview(self.frame_2, height=3, columns=('clo1', 'clo2', 'clo3','col4'))
        self.ListaCli.heading('#0', text='')
        self.ListaCli.heading('#1', text='Código')
        self.ListaCli.heading('#2', text='Nome')
        self.ListaCli.heading('#3', text='Telefone')
        self.ListaCli.heading('#4', text='Cidade')

        self.ListaCli.column('#0', width=1)
        self.ListaCli.column('#1', width=50)
        self.ListaCli.column('#2', width=200)
        self.ListaCli.column('#3', width=125)
        self.ListaCli.column('#4', width=125)

        self.ListaCli.place( relx=0.01, rely=0.1, relheight=0.85, relwidth=0.95)

        self.scrolLista = Scrollbar(self.frame_2, orient='vertical')
        self.ListaCli.configure(yscroll=self.scrolLista.set)
        self.scrolLista.place(relx=0.96, rely=0.1, relwidth=0.02, relheight=0.85)
    def widgets_frame_1_1(self):
        debcred = DebCred(self.dc())
        taxa = TaxaBandeira(self.bandeira(), int(self.parcelas()), debcred)
        lista = ldp(float(self.val_produto()), self.bandeira(), taxa)

        label = Label(self.frame_1_1,   
                      text= f'Lucro: R${lista[0]:.2f} \n    
                      Margem de lucro: {lista[1]:.2f}% \n Preço Ideal: R${lista[2]:.2f} \n    
                      Desconto Máximo: R${lista[3]:.2f} \n Lucro mínimo: R${lista[4]:.2f} \n    
                      Tarifa da maquininha: R${lista[5]:.2f} \n     
                      Parcelas: R${lista[2]/int(self.ent_par.get()):.2f}',    
                      bg ="#48D1CC", border= 5, foreground="#fff", font="ArialBlack")
        label.place(relx=0.02, relheight= 0.96, relwidth= 0.96)







Aplicativo()














