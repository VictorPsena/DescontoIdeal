import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def mostrar_grafico():
    # Exemplo de dados
    categorias = ['PIX', 'Débito', 'Crédito 1x', 'Crédito 12x']
    lucros = [185.67, 160.00, 140.00, 120.00]

    # Criar figura do Matplotlib
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(categorias, lucros, color='skyblue')
    ax.set_title('Lucro por forma de pagamento')
    ax.set_ylabel('Lucro (R$)')

    # Colocar gráfico no Tkinter
    canvas = FigureCanvasTkAgg(fig, master=janela)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=20)

# Criar janela principal
janela = tk.Tk()
janela.title("Análise de Lucro")

botao = tk.Button(janela, text="Mostrar Gráfico", command=mostrar_grafico)
botao.pack()

janela.mainloop()