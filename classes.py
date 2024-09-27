from datetime import datetime
import pprint
import logging


class Menu:

    def __init__(self, events):
        self.events = events

    def show_menu(self):
        print("==== MENU ====")
        print("1. Mostrar eventos do presidente.")
        print("2. Local mais comum dos eventos do presidente.")
        print("3. Qual é o próximo evento do presidente.")
        print("4. Print dos eventos por ordem alfabetica do título do evento.")
        print("5. Print dos eventos por ordem alfabetica do local do evento.")
        print("6. Print dos eventos ordenados por data (apenas o dia).")
        print("7. Print dos eventos ordenados por hora (apenas o horario).")
        print("0. Sair")
        print("==============")

    def show_events(self):  ## menu 1
        print("\nVocê escolheu a Opção 1!\n")
        pprint.pprint(f"{self.events}")
        return self.events

    def get_most_common_location(self):  ## menu2
        print("\nVocê escolheu a Opção 2!\n")
        locations = [evento["local"] for evento in self.events]
        most_frequented_locations = max(set(locations), key=locations.count)
        print(f"O local mais comum dos eventos é: {most_frequented_locations}")
        return most_frequented_locations

    def get_next_event(self):  ## menu 3
        print("\nVocê escolheu a Opção 3!\n")
        now = datetime.now()

        events_ordered_date = sorted(
            self.events, key=lambda x: (x["dia"], x["horario"])
        )

        for evento in events_ordered_date:
            day_hour = datetime.strptime(
                f"{evento['dia']} {evento['horario']}", "%Y-%m-%d %Hh%M"
            )
            if day_hour > now:
                logging.info("Found event: {}".format(evento))
                print(evento)
                return evento

    def events_alphabetically_title(self):  ## menu 4
        print("\nVocê escolheu a Opção 4!\n")
        events_ordered = sorted(self.events, key=lambda x: x["titulo"])
        print(events_ordered)
        return events_ordered

    def events_alphabetically_location(self):  ## menu 5
        print("\nVocê escolheu a Opção 5!\n")
        events_ordered_local = sorted(self.events, key=lambda x: x["local"])
        print(events_ordered_local)
        return events_ordered_local

    def events_ordered_date(self):  ## menu 6
        print("\nVocê escolheu a Opção 6!\n")
        events_ordered_date = sorted(self.events, key=lambda x: x["dia"])
        print(events_ordered_date)
        return events_ordered_date

    def events_ordered_hours(self):  ## menu 7
        print("\nVocê escolheu a Opção 7!\n")
        events_ordered_time = sorted(self.events, key=lambda x: x["horario"])
        print(events_ordered_time)
        return events_ordered_time

    def stop_program(self):
        print("\nObrigado!\n")

    def change_menu(self):
        while True:
            self.show_menu()
            choice = input("Escolha a opção desejada (0-7): ")

            if choice == "1":
                self.show_events()
            elif choice == "2":
                self.get_most_common_location()
            elif choice == "3":
                self.get_next_event()
            elif choice == "4":
                self.events_alphabetically_title()
            elif choice == "5":
                self.events_alphabetically_location()
            elif choice == "6":
                self.events_ordered_date()
            elif choice == "7":
                self.events_ordered_hours()
            elif choice == "0":
                self.stop_program()
                break
            else:
                print("Opção inválida! choice de 0 a 7.")
