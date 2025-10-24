import matplotlib.pyplot as plt
import locale
import matplotlib.ticker as ticker

# Configura para usar vírgula como separador decimal (pt_BR)
locale.setlocale(locale.LC_NUMERIC, 'pt_BR.UTF-8')

# Preço base
preco = 100.5
lucros = [preco, preco - 0.02*preco, preco - 0.05*preco, preco - 0.07*preco]
x = range(len(lucros))

# Cria o gráfico
fig, ax = plt.subplots()
ax.plot(x, lucros, marker='o')

# Formata os números do eixo y com vírgula
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: format(x, 'n')))

# Rótulos
plt.title("Lucros simulados")
plt.xlabel("Cenário")
plt.ylabel("Lucro")

plt.show()
