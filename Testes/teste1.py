import requests
from bs4 import BeautifulSoup
import pandas as pd

# Função para extrair o preço de um celular dado a URL e o seletor CSS
def get_price(url, css_selector):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    
    soup = BeautifulSoup(response.content, 'html.parser')
    element = soup.select_one(css_selector)
    
    if element:
        return element.text.strip()
    return None

# URLs e seletores CSS dos preços do Samsung Galaxy S20
products = [
    {"site": "Zoom", "url": "https://www.zoom.com.br/celular/samsung-galaxy-s20-128gb", "css_selector": ".price__SalesPrice-sc-1h98xa9-1"},
    {"site": "Buscapé", "url": "https://www.buscape.com.br/celular/samsung-galaxy-s20-128gb", "css_selector": ".mainValue"}
]

# Lista para armazenar os resultados
results = []

# Extraindo os preços
for product in products:
    price = get_price(product['url'], product['css_selector'])
    results.append({"Site": product['site'], "URL": product['url'], "Preço": price})

# Criando um DataFrame com os resultados
df = pd.DataFrame(results)

# Salvando os resultados em uma planilha Excel
df.to_excel("precos_samsung_s20.xlsx", index=False)

print("Os preços foram salvos em 'precos_samsung_s20.xlsx'")
