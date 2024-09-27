from classes import Menu
import json
import os


# Construir o caminho usando os.path.join
diretorio = r"C:/Users/gugui/Presidente_Agenda/"
nome_arquivo = "meu_arquivo_v1.json"

file_path = os.path.join(diretorio, nome_arquivo)

with open(file_path, "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

menu = Menu(dados)
menu.change_menu()
