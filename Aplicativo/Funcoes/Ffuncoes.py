########## FUNÇÕES QUE VOU UTILIZAR PARA CRIAR O APLICATIVO ##################################
from time import sleep

def Linhas2(tam = 29):
    print(tam*'=+')

def Linhas(msg):
    print('='*42)
    print(msg.center(42))
    print('='*42)

############################## verfica se o num é int ou float ###############################
def VerificaFloat(msg):
    while True:
        try:
            x = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO\033[m, Digite um valor válido')
            continue
        else:
            return x


def VerificaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('Erro, digite um valor inteiro')
            continue
        else:
            return n

##############################################################################################


######################### Qual é a bandeira do cartão ########################################
def VerficaBandeira(msg):
    while True:
        n = str(input(msg)).lower().strip()
        sleep(1)
        if n == 'visa':
            Linhas('A Bandeira escolida é \033[32mVISA\033[m!')
            return n
        elif n == 'mastercard':
            Linhas('A Bandeira escolida é \033[33mMASTERCARD\033[m!')
            return n
        elif n == 'elo':
            Linhas('A Bandeira escolida é \033[34mELO\033[m!')
            return n
        elif n == 'hipercard':
            Linhas('A Bandeira escolida é \033[33mHIPERCARD\033[m!')
            return n
        else:
            print('Bandeira do cartão não cadastrada.')
            continue
##############################################################################################


############################### Débito ou crédito ###########################################
# 7 siginifica que a compra será efetuada no crédito 
# 6 siginifica que a compra será efetuada no débito
def DebCred(msg):
    while True:
        n = str(input(msg)).upper().strip()[0] 
      
        if n =='C':
            x = 7
            return x
        elif n =='D':
            x = 6
            return x
        else:
            print('\033[31mOpção inválida\033[m, escolha entre crédito ou débito.')
            continue

# x = DebCred("Escolha: ")
# print(x)
##############################################################################################


#########################    Quantidade de parcelas ##########################################
def QuantidadeParcelas(msg):
    while True: 
        x = VerificaInt(msg)
        if 1 <= x <= 12:
            return x
        else:
            print("O máximo que conseguimos parcelar é 12 vezes.")
            continue

# x = QuantidadeParcelas("Quantidade de parcelas: ")
# print(x)

##############################################################################################


############ Mostra as taxas da bandeira escolida 2.0 tendo o número de parcelas #############

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
        if bandeira == 'visa' or bandeira == 'mastercard':
            if DebitoOuCredito == 7:
                for i in range(len(listaCreditoVM)):
                    if parcelas - 1 == i:
                        taxa = listaCreditoVM[i]
                        return taxa
                    else:
                        continue
            elif DebitoOuCredito == 6: # Será que tenho que adicionar um 'and parcelas = 1'?
                taxa = listaDebitoVM
                return taxa
            else:
                print("opção inválida")
                DebitoOuCredito = DebCred("Escolha entre Débito ou Crédito: ")
                continue
        elif bandeira == 'elo' or bandeira == 'hipercard':
            if DebitoOuCredito == 7:
                for i in range(len(listaCreditoEH)):
                    if parcelas - 1 == i:
                        taxa = listaCreditoEH[i]
                        return taxa
                    else:
                        continue
            elif DebitoOuCredito == 6:
                taxa = listaDebitoEH
                return taxa
            else:
                print("opção inválida")
                DebitoOuCredito = DebCred("Escolha entre Débito ou Crédito: ")
                continue



#x = TaxaBandeira('elo', 2, 7)

#print(x)

##############################################################################################


############################### Quantos produtos #############################################
def Quantidade(quant):
    val = int(input(quant))



##############################################################################################





############### Calcula o preço que o vendedor pode colocar no produto #######################

# Para definirmos nosso valor ideal do preço do produto temos que saber como a nossa loja funciona e com qual frequência o produto está sendo vendido, se estiver sendo muito vendido, podemos aumenter a nossa margem de lucro, se não, diminuir, se for muito dificil de produzir, podemos aumentar, e assim por diante. Temos vários fatores que acarretam na variação do lucro, mas, digamos que podemos definir uma margem de lucro depedendo do preço do produto, por exemplo, se o produto custa entre 0 < custo < 500 a margem de lucro é de 10% em cima do valor do produto, caso o valor aumente, eu posso diminuir a porcentagem, entretanto o lucro será maior.

# essa função calcula o lucro, desconto máximo e preço ideal para o produto ser vendido 


def ldp(ValorCompra,  bandeira, TaxaCartao):
    Lucro_Liq = 0
    Lucro_marg = 0
    desconMax = 0
    precos = 0

    while True:
        listapreco = [0.0369, 0.0599, 0.0629, 0.0715, 0.0799, 0.0879, 0.0959, 0.1039,  0.1119, 0.1199, 0.1279, 0.1349, 0.0488, 0.0738, 0.0768, 0.0854, 0.0938, 0.1018, 0.1098, 0.1178, 0.1258,  0.1338, 0.1418, 0.1488]
        if bandeira == 'visa' or bandeira == 'mastercard':
            
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
                
            else:
                 print("O Valor do produto excede os valores cadastrados ")
                 ValorCompra = int(input("Digite o valor da compra: "))
                 continue


        # Agora vamos fazer para as bandeira 'elo' e 'hipercard'

        elif bandeira == 'elo' or bandeira == 'hipercard':
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
            else:
                 print("O Valor do produto excede os valores cadastrados ")
                 ValorCompra = int(input("Digite o valor da compra: "))
                 continue

        else:
           print("\033[33mAlgum valor está errado\033[m")
           ValorCompra = int(input("Digite o valor da compra: "))
           bandeira = str(input("Informe a bandeira: ")).lower()
           continue


# opcao = 7
# taxa = TaxaBandeira('visa', 12, opcao )
# print(taxa)
# lista =ldp(200, 'visa', taxa )
# print(lista)
###############################################################################################