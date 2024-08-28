class Menu:
    
    def __init__(self, dados):
        self.dados = dados
    
    def mostrar_menu(self):
        print("==== MENU ====")
        print("1. Mostrar eventos do presidente.")
        print("2. Local mais comum dos eventos do presidente.")
        print("3. Qual é o próximo evento do presidente.")
        print('4. Sair')
        print("==============")
        
    def opcao_1(self):
        print("\nVocê escolheu a Opção 1!\n")
        
        for evento in self.dados:
            print(f"Dia: {evento['dia']},Titulo: {evento['titulo']}, Horário: {evento['horario']}, local: {evento['local']} ")
 
    def opcao_2(self):
        print("\nVocê escolheu a Opção 2!\n")
        
        locais = [evento['local'] for evento in self.dados]
        locais_mais_comuns = max(set(locais), key=locais.count)
        print(f'O local mais comum de eventos do presidente é: {locais_mais_comuns}')
        
    def opcao_3(self):
        print("\nVocê escolheu a Opção 3!\n")
        from datetime import datetime
        
        eventos_ordenados = sorted(self.dados, key=lambda e: datetime.strptime(f"{e['dia']} {e['horario']}", '%Y-%m-%d %Hh%M'))
        proximo_evento = eventos_ordenados[0]
        print(f'O próximo evento do presidente é: {proximo_evento}')
    
    def opcao_4(self):
        print("\nObrigado!\n")
        
    def escolha_menu(self):
        while True:
            self.mostrar_menu()
            escolha = input('Escolha a opção desejada (1-4): ')
            
            if escolha == '1':
                self.opcao_1()
            elif escolha == '2':
                self.opcao_2()
            elif escolha == '3':
                self.opcao_3()
            elif escolha == '4':
                self.opcao_4()
                break
            elif escolha != '1234':
                print('Opção inválida! Escolha de 1 a 4.')
            
                

