# Aqui, vou colocar todas as funções que utilizarei no para gerar o aplicativo

def TaxaBandeira(bandeira, parcelas, tipo_pagamento):
    # Mapeamento das taxas
    taxas = {
        'vm': {
            'credito': [0.0369, 0.0599, 0.0629, 0.0715, 0.0799, 0.0879, 
                        0.0959, 0.1039, 0.1119, 0.1199, 0.1279, 0.1349],
            'debito': 0.0179
        },
        'eh': {
            'credito': [0.0488, 0.0738, 0.0768, 0.0854, 0.0938, 0.1018,
                        0.1098, 0.1178, 0.1258, 0.1338, 0.1418, 0.1488],
            'debito': 0.0298
        }
    }
    
    # Determinar grupo de bandeiras
    grupo = 'vm' if bandeira in ['v', 'm'] else 'eh'
    
    # Determinar tipo de pagamento
    if tipo_pagamento == 'd':
        return taxas[grupo]['debito']
    elif tipo_pagamento == 'c' and 1 <= parcelas <= 12:
        return taxas[grupo]['credito'][parcelas - 1]
    
    return 0  # Valor padrão para casos inválidos
def calcular_precos(valor_compra, taxa_lucro):
    # Todas as taxas possíveis
    todas_taxas = [
        0.0369, 0.0599, 0.0629, 0.0715, 0.0799, 0.0879, 0.0959, 0.1039, 0.1119, 0.1199, 0.1279, 0.1349,
        0.0488, 0.0738, 0.0768, 0.0854, 0.0938, 0.1018, 0.1098, 0.1178, 0.1258, 0.1338, 0.1418, 0.1488
    ]
    
    # Preço mínimo de venda
    preco_minimo = valor_compra * (1 + taxa_lucro)
    
    # Calcular soma de preços considerando todas as taxas
    soma_precos = sum(taxa * preco_minimo + preco_minimo for taxa in todas_taxas)
    
    # Média de preços
    media_precos = soma_precos / len(todas_taxas)
    
    # Preço de venda estimado (considerando a maior taxa)
    preco_venda = media_precos + max(todas_taxas) * valor_compra
    
    return preco_minimo, preco_venda, media_precos
def ldp(valor_compra, bandeira, taxa_cartao):
    # Determinar taxa de lucro mínima baseada no valor e bandeira
    if bandeira in ['v', 'm']:
        if valor_compra < 500:
            taxa_lucro = 0.12
            margem_minima = 0.10
        elif valor_compra < 5000:
            taxa_lucro = 0.10
            margem_minima = 0.10
        else:
            taxa_lucro = 0.07
            margem_minima = 0.08
    else:  # Bandeeiras 'e' ou 'h'
        if valor_compra < 500:
            taxa_lucro = 0.12
            margem_minima = 0.10
        elif valor_compra < 5000:
            taxa_lucro = 0.10
            margem_minima = 0.08
        else:
            taxa_lucro = 0.08
            margem_minima = 0.05

    # Calcular valores base
    preco_pix, preco_venda, _ = calcular_precos(valor_compra, taxa_lucro)
    
    # Cálculos financeiros
    taxa_maquininha = preco_venda * taxa_cartao
    lucro_liquido = preco_venda - taxa_maquininha - valor_compra
    margem_lucro = lucro_liquido / preco_venda
    desconto_maximo = preco_venda - preco_pix - taxa_maquininha
    lucro_minimo = valor_compra * taxa_lucro

    # Verificar margem mínima
    if margem_lucro < margem_minima:
        return 1
    
    return [
        lucro_liquido,
        margem_lucro * 100,
        preco_venda,
        desconto_maximo,
        lucro_minimo,
        taxa_maquininha,
        preco_pix
    ]
