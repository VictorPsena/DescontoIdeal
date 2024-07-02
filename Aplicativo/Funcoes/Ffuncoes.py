# Aqui, vou colocar todas as funções que utilizarei no para gerar o aplicativo

def TaxaBandeira(bandeira, parcelas, DebitoOuCredito):
    # band = str(bandeira)
    # parc = int(parcelas)
    # as taxas das bandeiras são baseadas na maquininha ton no plano GigaTon
    taxa = 0
    listaCreditoVM = [0.0369, 0.0599, 0.0629, 0.0715, 0.0799, 0.0879, 0.0959, 0.1039,  0.1119, 0.1199, 0.1279, 0.1349]
    listaDebitoVM = 0.0179
    
    listaCreditoEH = [0.0488, 0.0738, 0.0768, 0.0854, 0.0938, 0.1018, 0.1098, 0.1178, 0.1258,  0.1338, 0.1418, 0.1488]
    listaDebitoEH = 0.0298
    while True:
        if bandeira == 'v' or bandeira == 'm':
            if DebitoOuCredito == 'c':
                for i in range(len(listaCreditoVM)):
                    if parcelas - 1 == i:
                        taxa = listaCreditoVM[i]
                        return taxa
                    else:
                        continue
            elif DebitoOuCredito == 'd': # Será que tenho que adicionar um 'and parcelas = 1'?
                taxa = listaDebitoVM
                return taxa
        elif bandeira == 'e' or bandeira == 'h':
            if DebitoOuCredito == 'c':
                for i in range(len(listaCreditoEH)):
                    if parcelas - 1 == i:
                        taxa = listaCreditoEH[i]
                        return taxa
                    else:
                        continue
            elif DebitoOuCredito == 'd':
                taxa = listaDebitoEH
                return taxa
        break
def ldp(ValorCompra,  bandeira, TaxaCartao):
    Lucro_Liq = 0
    Lucro_marg = 0
    desconMax = 0
    precos = 0

    while True:
        listapreco = [0.0369, 0.0599, 0.0629, 0.0715, 0.0799, 0.0879, 0.0959, 0.1039,  0.1119, 0.1199, 0.1279, 0.1349, 0.0488, 0.0738, 0.0768, 0.0854, 0.0938, 0.1018, 0.1098, 0.1178, 0.1258,  0.1338, 0.1418, 0.1488]
        if bandeira == 'v' or bandeira == 'm':
            
            if  0 < ValorCompra < 500: #grupo 1
                 taxa = 0.12 # em cada if a única coisa que muda é a taxa 
                 # Tem as taxas de todos os cartões.
                 for i in listapreco:
                     precos += i*(ValorCompra*taxa + ValorCompra) + (ValorCompra*taxa + ValorCompra) # o 'ValorCompra*taxa + valorCompra' é o meu valor mínimo da venda, ou seja, não posso ter um preço menor que esse.


                 mediaprecos = precos/len(listapreco) # Como eu não sei em qual bandeira o meu cliente vai comprar antes de anunciar o produto, faço uma previsão, pego todas as taxa do cartão e divido pela quantidade de taxas, obtendo assim uma média de preços.
                #  print(mediaprecos)
                 Val_Comp = ValorCompra 
                 ##########################################
                 Val_Pix = ValorCompra*taxa + ValorCompra 
                 #########################################
                 Val_Vend = mediaprecos + listapreco[23]*ValorCompra # Como obti a média de preços, caso o meu cliente queira comprar com a maior parcela tenho que fazer essa previsão na hora de inserir o preço. Então no caso do nosso programa, estamos sempre prevendo a maior parcela do cartão, que no nosso caso é 0.1488
                 Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp # onde muda
                 Lucro_marg = Lucro_Liq/Val_Vend
                 desconMax = Val_Vend - (ValorCompra*taxa + ValorCompra) - TaxaCartao*Val_Vend # o desconto máximo está deixando apenas os 12% de lucro mínimo para esse tipo de valor.
                 lucromin = ValorCompra*taxa
                 taxamaquina = Val_Vend*TaxaCartao
                 if Lucro_marg < 0.1:
                    return 1
                 else:
                    return [Lucro_Liq, Lucro_marg*100, Val_Vend, desconMax, lucromin, taxamaquina, Val_Pix ]

        
            elif  500 <= ValorCompra < 5000: #grupo 2 
                 taxa = 0.10 # aqui muda
                 for i in listapreco:
                     precos += i*(ValorCompra*taxa + ValorCompra) + (ValorCompra*taxa + ValorCompra)

                 
                 mediaprecos = precos/len(listapreco)
                 Val_Comp = ValorCompra
                 Val_Pix = ValorCompra*taxa + ValorCompra
                 Val_Vend = mediaprecos + listapreco[23]*ValorCompra
                 Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
                 Lucro_marg = Lucro_Liq/Val_Vend
                 desconMax = Val_Vend - (ValorCompra*taxa + ValorCompra) - TaxaCartao*Val_Vend
                 lucromin = ValorCompra*taxa
                 taxamaquina = Val_Vend*TaxaCartao
                 if Lucro_marg < 0.1:
                    return 1
                 else:
                    return [Lucro_Liq, Lucro_marg*100, Val_Vend, desconMax, lucromin, taxamaquina, Val_Pix ]
        
            elif  5000 <= ValorCompra <= 50000: #grupo 3
                 taxa = 0.07 # aqui muda
                 for i in listapreco:
                     precos += i*(ValorCompra*taxa + ValorCompra) + (ValorCompra*taxa + ValorCompra)

                 
                 mediaprecos = precos/len(listapreco)
                 Val_Comp = ValorCompra
                 Val_Pix = ValorCompra*taxa + ValorCompra
                 Val_Vend = mediaprecos + listapreco[23]*ValorCompra
                 Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
                 Lucro_marg = Lucro_Liq/Val_Vend
                 desconMax = Val_Vend - (ValorCompra*taxa + ValorCompra) - TaxaCartao*Val_Vend
                 lucromin = ValorCompra*taxa
                 taxamaquina = Val_Vend*TaxaCartao

                 if Lucro_marg < 0.08:
                    return 1
                 else:
                    return [Lucro_Liq, Lucro_marg*100, Val_Vend, desconMax, lucromin, taxamaquina, Val_Pix ]
                

        elif bandeira == 'e' or bandeira == 'h':
            if 0 < ValorCompra < 500:
                    taxa = 0.12
                    for i in listapreco:
                     precos += i*(ValorCompra*taxa + ValorCompra) + (ValorCompra*taxa + ValorCompra)

                 
                    mediaprecos = precos/len(listapreco)
                    Val_Comp = ValorCompra
                    Val_Pix = ValorCompra*taxa + ValorCompra
                    Val_Vend = mediaprecos + listapreco[23]*ValorCompra
                    Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
                    Lucro_marg = Lucro_Liq/Val_Vend
                    desconMax = Val_Vend - (ValorCompra*taxa + ValorCompra) - TaxaCartao*Val_Vend
                    lucromin = ValorCompra*taxa
                    taxamaquina = Val_Vend*TaxaCartao
                    if Lucro_marg < 0.1:
                        return 1
                    else:
                        return [Lucro_Liq, Lucro_marg*100, Val_Vend, desconMax, lucromin, taxamaquina, Val_Pix ]


            elif  500 <= ValorCompra < 5000:
                    taxa = 0.10
                    for i in listapreco:
                     precos += i*(ValorCompra*taxa + ValorCompra) + (ValorCompra*taxa + ValorCompra)

                 
                    mediaprecos = precos/len(listapreco)
                    Val_Comp = ValorCompra
                    Val_Pix = ValorCompra*taxa + ValorCompra
                    Val_Vend = mediaprecos + listapreco[23]*ValorCompra
                    Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
                    Lucro_marg = Lucro_Liq/Val_Vend
                    desconMax = Val_Vend - (ValorCompra*taxa + ValorCompra) - TaxaCartao*Val_Vend
                    lucromin = ValorCompra*taxa
                    taxamaquina = Val_Vend*TaxaCartao

                    if Lucro_marg < 0.08:
                        return 1
                    
                    else:
                        return [Lucro_Liq, Lucro_marg*100, Val_Vend, desconMax, lucromin, taxamaquina, Val_Pix ]

            elif 5000 <= ValorCompra <= 50000:
                    taxa = 0.08
                    for i in listapreco:
                     precos += i*(ValorCompra*taxa + ValorCompra) + (ValorCompra*taxa + ValorCompra)

                 
                    mediaprecos = precos/len(listapreco)
                    Val_Comp = ValorCompra
                    Val_Pix = ValorCompra*taxa + ValorCompra
                    Val_Vend = mediaprecos + listapreco[22]*ValorCompra
                    Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
                    Lucro_marg = Lucro_Liq/Val_Vend
                    desconMax = Val_Vend - (ValorCompra*taxa + ValorCompra) - TaxaCartao*Val_Vend
                    lucromin = ValorCompra*taxa
                    taxamaquina = Val_Vend*TaxaCartao

                    if Lucro_marg < 0.05:
                        return 1

                    else:
                        return [Lucro_Liq, Lucro_marg*100, Val_Vend, desconMax, lucromin, taxamaquina, Val_Pix ]

        break

#print(ldp(1000, 'e', 0.0629))
#print(TaxaBandeira('e', 12, 'c'))


  #  def ldp(self, ValorCompra,  bandeira, TaxaCartao):

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
                    

    #def TaxaBandeira(self, bandeira, parcelas, DebitoOuCredito):
        self.taxa = 0
        self.listaCreditoVM = [0.0369, 0.0599, 0.0629, 0.0715, 0.0799, 0.0879, 0.0959, 0.1039,  0.1119, 0.1199, 0.1279, 0.1349]
        self.listaDebitoVM = 0.0179
        
        self.listaCreditoEH = [0.0488, 0.0738, 0.0768, 0.0854, 0.0938, 0.1018, 0.1098, 0.1178, 0.1258,  0.1338, 0.1418, 0.1488]
        self.listaDebitoEH = 0.0298
        while True:
            if bandeira == 'v' or bandeira == 'm':
                if DebitoOuCredito == 'c':
                    for i in range(len(self.listaCreditoVM)):
                        if parcelas - 1 == i:
                            self.taxa = self.listaCreditoVM[i]
                            return self.taxa
                        else:
                            break
                elif self.DebitoOuCredito == 'd': # Será que tenho que adicionar um 'and parcelas = 1'?
                    self.taxa = self.listaDebitoVM
                    return self.taxa

            elif bandeira == 'e' or bandeira == 'h':
                if DebitoOuCredito == 'c':
                    for i in range(len(self.listaCreditoEH)):
                        if parcelas - 1 == i:
                            self.taxa = self.listaCreditoEH[i]
                            return self.taxa
                        else:
                            break
                elif DebitoOuCredito == 'd':
                    self.taxa = self.listaDebitoEH
                    return self.taxa
            break