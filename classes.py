from datetime import datetime
import pprint

class Menu:
    
    def __init__(self, dados):
        self.dados = dados
    
    def mostrar_menu(self):
        print("==== MENU ====")
        print("1. Mostrar eventos do presidente.")
        print("2. Local mais comum dos eventos do presidente.")
        print("3. Qual é o próximo evento do presidente.")
        print("4. Print dos eventos por ordem alfabetica do título do evento.")
        print("5. Print dos eventos por ordem alfabetica do local do evento.")
        print("6. Print dos eventos ordenados por data (apenas o dia).")
        print("7. Print dos eventos ordenados por hora (apenas o horario).")
        print('0. Sair')
        print("==============")
        
    def opcao_1(self):
        
        print("\nVocê escolheu a Opção 1!\n")
        pprint.pprint(f"{self.dados}")
        

    def opcao_2(self):
        print("\nVocê escolheu a Opção 2!\n")
        locais = [evento['local'] for evento in self.dados]
        local_mais_frequentados = max(set(locais), key=locais.count)
        print(f"O local mais comum dos eventos é: {local_mais_frequentados}")

    
    def opcao_3(self):
        print("\nVocê escolheu a Opção 3!\n")
        proximos_eventos = []
        agora = datetime.now()

        eventos_ordenados_data = sorted(self.dados, key=lambda x: (x['dia'], x['horario']))
        
        for evento in eventos_ordenados_data:
            dia_hora = datetime.strptime(f"{evento['dia']} {evento['horario']}", '%Y-%m-%d %Hh%M')
            if dia_hora > agora:
                proximos_eventos.append(evento)
                break
            
        if proximos_eventos:
            print(proximos_eventos)
        else:
            print("Eventos já realizados ou não disponíveis.")

                  
    def opcao_4(self):
        print("\nVocê escolheu a Opção 4!\n")
        eventos_ordenados = sorted(self.dados, key=lambda x: x['titulo'])
        print(eventos_ordenados)
        
    def opcao_5(self):
        print("\nVocê escolheu a Opção 5!\n")
        eventos_ordenados_local = sorted(self.dados, key=lambda x: x['local'])
        print(eventos_ordenados_local)
        
    def opcao_6(self):
        print("\nVocê escolheu a Opção 6!\n")
        eventos_ordenados_data = sorted(self.dados, key=lambda x: x['dia'])
        print(eventos_ordenados_data)
        
        
    def opcao_7(self):
        print("\nVocê escolheu a Opção 7!\n")
        eventos_ordenados_horario = sorted(self.dados, key=lambda x: x['horario'])
        print(eventos_ordenados_horario)
        
    
    def opcao_0(self):
        print("\nObrigado!\n")
        
    def escolha_menu(self):
        while True:
            self.mostrar_menu()
            escolha = input('Escolha a opção desejada (0-7): ')
            
            if escolha == '1':
                self.opcao_1()
            elif escolha == '2':
                self.opcao_2()
            elif escolha == '3':
                self.opcao_3()
            elif escolha == '4':
                self.opcao_4()
            elif escolha == '5':
                self.opcao_5()
            elif escolha == '6':
                self.opcao_6()
            elif escolha == '7':
                self.opcao_7()
            elif escolha == '0':
                self.opcao_0()
                break
            else:
                print('Opção inválida! Escolha de 0 a 7.')
                

