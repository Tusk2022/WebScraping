import requests
from bs4 import BeautifulSoup

url = 'https://www.telhanorte.com.br/resultado-busca?q=porcelanato&origin=autocomplete&apikey=telhanorte&terms=porcelanato&ranking=1&topsearch=1'

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 OPR/96.0.0.0"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
porcelanato = soup.find_all('div', 'x-shelf__title')
