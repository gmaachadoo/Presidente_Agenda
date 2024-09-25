import argparse
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta


def convert_date(date_str):
    try:
        return datetime.strptime(date_str, "%d/%m/%Y")
    except ValueError:
        raise ValueError("Formato de data inválido. Use o formato DD/MM/AAAA.")


parser = argparse.ArgumentParser(
    description="Extrair compromissos das datas específicas."
)
parser.add_argument(
    "--start_date", type=str, required=True, help="Data no formato DD/MM/AAAA"
)
parser.add_argument(
    "--end_date", type=str, required=True, help="Data no formato DD/MM/AAAA"
)

args = parser.parse_args()
start_date = convert_date(args.start_date)
end_date = convert_date(args.end_date)

if start_date > end_date:
    raise ValueError("A data de início não pode ser posterior à data de fim.")

commitments_list = []

current_date = start_date

while current_date <= end_date:
    data = current_date.strftime("%Y-%m-%d")

    url = f"https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/agenda-do-presidente-da-republica-lula/agenda-do-presidente-da-republica/{data}"
    response = requests.get(url)
    content = response.content

    site = BeautifulSoup(content, "html.parser")
    commitments = site.findAll("li", class_="item-compromisso-wrapper")

    for (
        commitment
    ) in (
        commitments
    ):  # vou adicionar esse for dentro de um outro for que vai alterando até a data desejada
        title = commitment.find("h2", class_="compromisso-titulo").text
        time = commitment.find("time", class_="compromisso-inicio").text
        location = commitment.find("div", class_="compromisso-local").text

        commitments_list.append(
            {"dia": data, "titulo": title, "horario": time, "local": location}
        )

    current_date += timedelta(days=1)


with open("meu_arquivo_v1.json", "w", encoding="utf-8") as arquivo_json:
    json.dump(commitments_list, arquivo_json, ensure_ascii=False, indent=4)
