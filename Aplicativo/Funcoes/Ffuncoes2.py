from tkinter import*
from tkinter import ttk
import sqlite3
from Ffuncoes import *
root = Tk()

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
    # def TaxaBandeira(self, bandeira, parcelas, DebitoOuCredito):
    #     self.taxa = 0
    #     self.listaCreditoVM = [0.0369, 0.0599, 0.0629, 0.0715, 0.0799, 0.0879, 0.0959, 0.1039,  0.1119, 0.1199, 0.1279, 0.1349]
    #     self.listaDebitoVM = 0.0179
        
    #     self.listaCreditoEH = [0.0488, 0.0738, 0.0768, 0.0854, 0.0938, 0.1018, 0.1098, 0.1178, 0.1258,  0.1338, 0.1418, 0.1488]
    #     self.listaDebitoEH = 0.0298
    #     while True:
    #         if bandeira == 'v' or bandeira == 'm':
    #             if DebitoOuCredito == 'c':
    #                 for i in range(len(self.listaCreditoVM)):
    #                     if parcelas - 1 == i:
    #                         self.taxa = self.listaCreditoVM[i]
    #                         return self.taxa
    #                     else:
    #                         break
    #             elif self.DebitoOuCredito == 'd': # Será que tenho que adicionar um 'and parcelas = 1'?
    #                 self.taxa = self.listaDebitoVM
    #                 return self.taxa

    #         elif bandeira == 'e' or bandeira == 'h':
    #             if DebitoOuCredito == 'c':
    #                 for i in range(len(self.listaCreditoEH)):
    #                     if parcelas - 1 == i:
    #                         self.taxa = self.listaCreditoEH[i]
    #                         return self.taxa
    #                     else:
    #                         break
    #             elif DebitoOuCredito == 'd':
    #                 self.taxa = self.listaDebitoEH
    #                 return self.taxa
    #         break
    # def ldp(self, ValorCompra,  bandeira, TaxaCartao):
        self.Lucro_Liq = 0
        self.Lucro_marg = 0
        self.desconMax = 0
        self.precos = 0

        while True:
            self.listapreco = [0.0369, 0.0599, 0.0629, 0.0715, 0.0799, 0.0879, 0.0959, 0.1039,  0.1119, 0.1199, 0.1279, 0.1349, 0.0488, 0.0738, 0.0768, 0.0854, 0.0938, 0.1018, 0.1098, 0.1178, 0.1258,  0.1338, 0.1418, 0.1488]
            if bandeira == 'v' or bandeira == 'm':
                
                if  0 < ValorCompra < 500: #grupo 1
                    self.taxa = 0.12 # em cada if a única coisa que muda é a taxa 
                    # Tem as taxas de todos os cartões.
                    for i in self.listapreco:
                        self.precos += i*(ValorCompra*self.taxa + ValorCompra) + (ValorCompra*self.taxa + ValorCompra) # o 'ValorCompra*taxa + valorCompra' é o meu valor mínimo da venda, ou seja, não posso ter um preço menor que esse.
                    self.mediaprecos = self.precos/len(self.listapreco) # Como eu não sei em qual bandeira o meu cliente vai comprar antes de anunciar o produto, faço uma previsão, pego todas as taxa do cartão e divido pela quantidade de taxas, obtendo assim uma média de preços.
                    #  print(mediaprecos)
                    self.Val_Comp = ValorCompra 
                    self.Val_Vend = self.mediaprecos + self.listapreco[23]*ValorCompra # Como obti a média de preços, caso o meu cliente queira comprar com a maior parcela tenho que fazer essa previsão na hora de inserir o preço. Então no caso do nosso programa, estamos sempre prevendo a maior parcela do cartão, que no nosso caso é 0.1488
                    self.Lucro_Liq = self.Val_Vend - TaxaCartao*self.Val_Vend - self.Val_Comp # onde muda
                    self.Lucro_marg = self.Lucro_Liq/self.Val_Vend
                    self.desconMax = self.Val_Vend - (ValorCompra*self.taxa + ValorCompra) - TaxaCartao*self.Val_Vend # o desconto máximo está deixando apenas os 12% de lucro mínimo para esse tipo de valor.
                    self.lucromin = ValorCompra*self.taxa
                    self.taxamaquina = self.Val_Vend*TaxaCartao
                    if self.Lucro_marg < 0.1:
                        return 1
                    else:
                        return [self.Lucro_Liq, self.Lucro_marg*100, self.Val_Vend, self.desconMax, self.lucromin, self.taxamaquina ]

            
                elif  500 <= ValorCompra < 5000: #grupo 2 
                    self.taxa = 0.10 # aqui muda
                    for i in self.listapreco:
                        self.precos += i*(ValorCompra*self.taxa + ValorCompra) + (ValorCompra*self.taxa + ValorCompra) 
                    self.mediaprecos = self.precos/len(self.listapreco) 
                    self.Val_Comp = ValorCompra 
                    self.Val_Vend = self.mediaprecos + self.listapreco[23]*ValorCompra 
                    self.Lucro_Liq = self.Val_Vend - TaxaCartao*self.Val_Vend - self.Val_Comp 
                    self.Lucro_marg = self.Lucro_Liq/self.Val_Vend
                    self.desconMax = self.Val_Vend - (ValorCompra*self.taxa + ValorCompra) - TaxaCartao*self.Val_Vend 
                    self.lucromin = ValorCompra*self.taxa
                    self.taxamaquina = self.Val_Vend*TaxaCartao
                    if self.Lucro_marg < 0.1:
                        return 1
                    else:
                        return [self.Lucro_Liq, self.Lucro_marg*100, self.Val_Vend, self.desconMax, self.lucromin, self.taxamaquina ]
            
                elif  5000 <= ValorCompra <= 50000: #grupo 3
                    self.taxa = 0.07 # aqui muda
                    for i in self.listapreco:
                        self.precos += i*(ValorCompra*self.taxa + ValorCompra) + (ValorCompra*self.taxa + ValorCompra) 
                    self.mediaprecos = self.precos/len(self.listapreco) 
                    self.Val_Comp = ValorCompra 
                    self.Val_Vend = self.mediaprecos + self.listapreco[23]*ValorCompra 
                    self.Lucro_Liq = self.Val_Vend - TaxaCartao*self.Val_Vend - self.Val_Comp 
                    self.Lucro_marg = self.Lucro_Liq/self.Val_Vend
                    self.desconMax = self.Val_Vend - (ValorCompra*self.taxa + ValorCompra) - TaxaCartao*self.Val_Vend 
                    self.lucromin = ValorCompra*self.taxa
                    self.taxamaquina = self.Val_Vend*TaxaCartao
                    if self.Lucro_marg < 0.08:
                        return 1
                    else:
                        return [self.Lucro_Liq, self.Lucro_marg*100, self.Val_Vend, self.desconMax, self.lucromin, self.taxamaquina ]
                    


            # Agora vamos fazer para as bandeira 'elo' e 'hipercard'

            elif bandeira == 'e' or bandeira == 'h':
                if 0 < ValorCompra < 500:
                    self.taxa = 0.12
                    for i in self.listapreco:
                        self.precos += i*(ValorCompra*self.taxa + ValorCompra) + (ValorCompra*self.taxa + ValorCompra) 
                    self.mediaprecos = self.precos/len(self.listapreco) 
                    self.Val_Comp = ValorCompra 
                    self.Val_Vend = self.mediaprecos + self.listapreco[23]*ValorCompra 
                    self.Lucro_Liq = self.Val_Vend - TaxaCartao*self.Val_Vend - self.Val_Comp 
                    self.Lucro_marg = self.Lucro_Liq/self.Val_Vend
                    self.desconMax = self.Val_Vend - (ValorCompra*self.taxa + ValorCompra) - TaxaCartao*self.Val_Vend 
                    self.lucromin = ValorCompra*self.taxa
                    self.taxamaquina = self.Val_Vend*TaxaCartao
                    if self.Lucro_marg < 0.1:
                        return 1
                    else:
                        return [self.Lucro_Liq, self.Lucro_marg*100, self.Val_Vend, self.desconMax, self.lucromin, self.taxamaquina ]


                elif  500 <= ValorCompra < 5000:
                    self.taxa = 0.10
                    for i in self.listapreco:
                        self.precos += i*(ValorCompra*self.taxa + ValorCompra) + (ValorCompra*self.taxa + ValorCompra) 
                    self.mediaprecos = self.precos/len(self.listapreco) 
                    self.Val_Comp = ValorCompra 
                    self.Val_Vend = self.mediaprecos + self.listapreco[23]*ValorCompra 
                    self.Lucro_Liq = self.Val_Vend - TaxaCartao*self.Val_Vend - self.Val_Comp 
                    self.Lucro_marg = self.Lucro_Liq/self.Val_Vend
                    self.desconMax = self.Val_Vend - (ValorCompra*self.taxa + ValorCompra) - TaxaCartao*self.Val_Vend 
                    self.lucromin = ValorCompra*self.taxa
                    self.taxamaquina = self.Val_Vend*TaxaCartao
                    if self.Lucro_marg < 0.08:
                        return 1
                    else:
                        return [self.Lucro_Liq, self.Lucro_marg*100, self.Val_Vend, self.desconMax, self.lucromin, self.taxamaquina ]

                elif 5000 <= ValorCompra <= 50000:
                    self.taxa = 0.08
                    for i in self.listapreco:
                        self.precos += i*(ValorCompra*self.taxa + ValorCompra) + (ValorCompra*self.taxa + ValorCompra) 
                    self.mediaprecos = self.precos/len(self.listapreco) 
                    self.Val_Comp = ValorCompra 
                    self.Val_Vend = self.mediaprecos + self.listapreco[23]*ValorCompra 
                    self.Lucro_Liq = self.Val_Vend - TaxaCartao*self.Val_Vend - self.Val_Comp 
                    self.Lucro_marg = self.Lucro_Liq/self.Val_Vend
                    self.desconMax = self.Val_Vend - (ValorCompra*self.taxa + ValorCompra) - TaxaCartao*self.Val_Vend 
                    self.lucromin = ValorCompra*self.taxa
                    self.taxamaquina = self.Val_Vend*TaxaCartao
                    if self.Lucro_marg < 0.1:
                        return 1
                    else:
                        return [self.Lucro_Liq, self.Lucro_marg*100, self.Val_Vend, self.desconMax, self.lucromin, self.taxamaquina ]
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

        self.label = Label(self.frame_1_1,   
                      text= f'Lucro: R${self.lista[0]:.2f} \n Margem de lucro: {self.lista[1]:.2f}% \n Preço Ideal: R${self.lista[2]:.2f} \n  Desconto Máximo: R${self.lista[3]:.2f} \n Lucro mínimo: R${self.lista[4]:.2f} \n Tarifa da maquininha: R${self.lista[5]:.2f} \n Parcelas: R${self.lista[2]/int(self.ent_par.get()):.2f}',    
                      bg ="#48D1CC", border= 5, foreground="#fff", font="ArialBlack")
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
                                fg='White', font=('verdana', 8, 'bold'), command=self.widgets_frame_1_1)
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






Aplicativo()














