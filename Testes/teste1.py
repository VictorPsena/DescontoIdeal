import pandas as pd

# Dados de exemplo
dados = {
    'Nome': ['João', 'Maria', 'Pedro'],
    'Idade': [25, 30, 35],
    'Sexo': ['Masculino', 'Feminino', 'Masculino']
}

# Criar um DataFrame a partir dos dados
df = pd.DataFrame(dados)

# Salvar o DataFrame em um arquivo Excel
df.to_excel('planilha.xlsx', index=False)
