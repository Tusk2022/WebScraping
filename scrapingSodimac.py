import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import math

url = 'https://www.sodimac.com.br/sodimac-br/category/cat170729/porcelanato/'

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 OPR/96.0.0.0"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
qtd_itens = soup.find('div', class_="category-product-count").get_text().strip()

index = qtd_itens.find(' ')
qtd = qtd_itens[:index]
qtd = qtd[1:]

ultima_pagina = math.ceil(int(qtd) / 28)

dic_produtos = {'marca': [], 'preco': []}

for i in range(1, ultima_pagina+1):
    url_pag = f'https://www.sodimac.com.br/sodimac-br/category/cat170729/porcelanato?currentpage={i}'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    produtos = soup.find_all('div', class_=re.compile('product-wrapper'))

    for produto in produtos:
        marca = produto.find('h2', class_=re.compile('product-title')).get_text().strip()
        preco = produto.find('div', class_=re.compile('mobile-price-details')).get_text().strip()

        print(marca, preco)

        dic_produtos['marca'].append(marca)
        dic_produtos['preco'].append(preco)

    print(url_pag)


df = pd.DataFrame(dic_produtos)
df.to_csv('C:/Users/rodri/Downloads/Preco_Porcelanato.csv', encoding='utf-8', sep=';')
