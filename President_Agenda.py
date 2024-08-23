import argparse
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

parser = argparse.ArgumentParser(description='Extrair compromissos para uma data específica.')
parser.add_argument('--data', type=str, required=True, help='Data no formato DD/MM/AAAA')

args = parser.parse_args()
data_str = args.data

try:
    data = datetime.strptime(data_str, '%d/%m/%Y').strftime('%Y-%m-%d')
except ValueError:
    print("Formato de data inválido. Use o formato DD/MM/AAAA.")
    exit(1)


url = f'https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/agenda-do-presidente-da-republica-lula/agenda-do-presidente-da-republica/{data}'


response = requests.get(url)
content = response.content

site = BeautifulSoup(content, 'html.parser')

commitments = site.findAll('li', class_='item-compromisso-wrapper')
commitments_list = []

for commitment in commitments:
    title = commitment.find('h2', class_='compromisso-titulo').text
    time = commitment.find('time', class_='compromisso-inicio').text
    location = commitment.find('div', class_='compromisso-local').text
    
    
    commitments_list.append({
        'titulo': title,
        'horario': time,
        'local': location
    })
    

with open('meu_arquivo_v1.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(commitments_list, arquivo_json, ensure_ascii=False, indent=4)








