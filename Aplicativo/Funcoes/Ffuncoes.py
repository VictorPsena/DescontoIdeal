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
                 Val_Vend = mediaprecos + listapreco[23]*ValorCompra # Como obti a média de preços, caso o meu cliente queira comprar com a maior parcela tenho que fazer essa previsão na hora de inserir o preço. Então no caso do nosso programa, estamos sempre prevendo a maior parcela do cartão, que no nosso caso é 0.1488
                 Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp # onde muda
                 Lucro_marg = Lucro_Liq/Val_Vend
                 desconMax = Val_Vend - (ValorCompra*taxa + ValorCompra) - TaxaCartao*Val_Vend # o desconto máximo está deixando apenas os 12% de lucro mínimo para esse tipo de valor.
                 lucromin = ValorCompra*taxa
                 taxamaquina = Val_Vend*TaxaCartao
                 if Lucro_marg < 0.1:
                    return 1
                 else:
                    return [Lucro_Liq, Lucro_marg*100, Val_Vend, desconMax, lucromin, taxamaquina ]

        
            elif  500 <= ValorCompra < 5000: #grupo 2 
                 taxa = 0.10 # aqui muda
                 for i in listapreco:
                     precos += i*(ValorCompra*taxa + ValorCompra) + (ValorCompra*taxa + ValorCompra)

                 
                 mediaprecos = precos/len(listapreco)
                 Val_Comp = ValorCompra
                 Val_Vend = mediaprecos + listapreco[23]*ValorCompra
                 Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
                 Lucro_marg = Lucro_Liq/Val_Vend
                 desconMax = Val_Vend - (ValorCompra*taxa + ValorCompra) - TaxaCartao*Val_Vend
                 lucromin = ValorCompra*taxa
                 taxamaquina = Val_Vend*TaxaCartao
                 if Lucro_marg < 0.1:
                    return 1
                 else:
                    return [Lucro_Liq, Lucro_marg*100, Val_Vend, desconMax, lucromin, taxamaquina ]
        
            elif  5000 <= ValorCompra <= 50000: #grupo 3
                 taxa = 0.07 # aqui muda
                 for i in listapreco:
                     precos += i*(ValorCompra*taxa + ValorCompra) + (ValorCompra*taxa + ValorCompra)

                 
                 mediaprecos = precos/len(listapreco)
                 Val_Comp = ValorCompra
                 Val_Vend = mediaprecos + listapreco[23]*ValorCompra
                 Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
                 Lucro_marg = Lucro_Liq/Val_Vend
                 desconMax = Val_Vend - (ValorCompra*taxa + ValorCompra) - TaxaCartao*Val_Vend
                 lucromin = ValorCompra*taxa
                 taxamaquina = Val_Vend*TaxaCartao

                 if Lucro_marg < 0.08:
                    return 1
                 else:
                    return [Lucro_Liq, Lucro_marg*100, Val_Vend, desconMax, lucromin, taxamaquina ]
                

        elif bandeira == 'e' or bandeira == 'h':
            if 0 < ValorCompra < 500:
                    taxa = 0.12
                    for i in listapreco:
                     precos += i*(ValorCompra*taxa + ValorCompra) + (ValorCompra*taxa + ValorCompra)

                 
                    mediaprecos = precos/len(listapreco)
                    Val_Comp = ValorCompra
                    Val_Vend = mediaprecos + listapreco[23]*ValorCompra
                    Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
                    Lucro_marg = Lucro_Liq/Val_Vend
                    desconMax = Val_Vend - (ValorCompra*taxa + ValorCompra) - TaxaCartao*Val_Vend
                    lucromin = ValorCompra*taxa
                    taxamaquina = Val_Vend*TaxaCartao
                    if Lucro_marg < 0.1:
                        return 1
                    else:
                        return [Lucro_Liq, Lucro_marg*100, Val_Vend, desconMax, lucromin, taxamaquina ]


            elif  500 <= ValorCompra < 5000:
                    taxa = 0.10
                    for i in listapreco:
                     precos += i*(ValorCompra*taxa + ValorCompra) + (ValorCompra*taxa + ValorCompra)

                 
                    mediaprecos = precos/len(listapreco)
                    Val_Comp = ValorCompra
                    Val_Vend = mediaprecos + listapreco[23]*ValorCompra
                    Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
                    Lucro_marg = Lucro_Liq/Val_Vend
                    desconMax = Val_Vend - (ValorCompra*taxa + ValorCompra) - TaxaCartao*Val_Vend
                    lucromin = ValorCompra*taxa
                    taxamaquina = Val_Vend*TaxaCartao

                    if Lucro_marg < 0.08:
                        return 1
                    
                    else:
                        return [Lucro_Liq, Lucro_marg*100, Val_Vend, desconMax, lucromin, taxamaquina ]

            elif 5000 <= ValorCompra <= 50000:
                    taxa = 0.08
                    for i in listapreco:
                     precos += i*(ValorCompra*taxa + ValorCompra) + (ValorCompra*taxa + ValorCompra)

                 
                    mediaprecos = precos/len(listapreco)
                    Val_Comp = ValorCompra
                    Val_Vend = mediaprecos + listapreco[22]*ValorCompra
                    Lucro_Liq = Val_Vend - TaxaCartao*Val_Vend - Val_Comp
                    Lucro_marg = Lucro_Liq/Val_Vend
                    desconMax = Val_Vend - (ValorCompra*taxa + ValorCompra) - TaxaCartao*Val_Vend
                    lucromin = ValorCompra*taxa
                    taxamaquina = Val_Vend*TaxaCartao

                    if Lucro_marg < 0.05:
                        return 1

                    else:
                        return [Lucro_Liq, Lucro_marg*100, Val_Vend, desconMax, lucromin, taxamaquina ]

        break

#print(ldp(1000, 'e', 0.0629))
#print(TaxaBandeira('e', 12, 'c'))