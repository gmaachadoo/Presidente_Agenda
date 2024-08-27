class Menu:
    
    def mostrar_menu(self):
        print("==== MENU ====")
        print("1. Mostrar eventos do presidente.")
        print("2. Local mais comum dos eventos do presidente.")
        print("3. Qual é o próximo evento do presidente.")
        print('4. Sair')
        print("==============")
        
    def opcao_1(self):
        print("\nVocê escolheu a Opção 1!\n")

    def opcao_2(self):
        print("\nVocê escolheu a Opção 2!\n")
        
    def opcao_3(self):
        print("\nVocê escolheu a Opção 3!\n")
    
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
                

