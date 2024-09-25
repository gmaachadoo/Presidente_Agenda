import unittest
import json

from freezegun import freeze_time

from classes import Menu


class TestMenu(unittest.TestCase):

    def test_show_events(self):
        with open("agenda_teste.json", "r", encoding="utf-8") as arquivo:
            events = json.load(arquivo)

        menu = Menu(events)
        expected_resut = [
            {
                "dia": "2024-09-02",
                "titulo": "A - Reunião",
                "horario": "09h00",
                "local": "Palácio do Planalto",
            },
            {
                "dia": "2024-09-02",
                "titulo": "D - Ministra do Meio Ambiente e Mudança do Clima, Marina Silva",
                "horario": "11h00",
                "local": "Palácio do Planalto",
            },
            {
                "dia": "2024-09-08",
                "titulo": "B - ESTE EVENTO",
                "horario": "02h30",
                "local": "Palácio do Planalto",
            },
            {
                "dia": "2024-09-08",
                "titulo": "C - EVENTO 2 APARECER",
                "horario": "05h30",
                "local": "Palácio do Planalto",
            },
        ]

        self.assertEqual(menu.show_events(), expected_resut)

    def test_get_most_common_location(self):
        with open("agenda_teste.json", "r", encoding="utf-8") as arquivo:
            events = json.load(arquivo)

        menu = Menu(events)

        expected_result = "Palácio do Planalto"
        self.assertEqual(menu.get_most_common_location(), expected_result)

    @freeze_time("2024-09-03")
    def test_get_next_event(self):
        with open("agenda_teste.json", "r", encoding="utf-8") as arquivo:
            events = json.load(arquivo)

        menu = Menu(events)

        expected_result = {
            "dia": "2024-09-08",
            "titulo": "B - ESTE EVENTO",
            "horario": "02h30",
            "local": "Palácio do Planalto",
        }

        self.assertEqual(menu.get_next_event(), expected_result)

    def test_events_alphabetically_title(self):
        with open("agenda_teste.json", "r", encoding="utf-8") as arquivo:
            events = json.load(arquivo)

        menu = Menu(events)
        expected_result = [
            {
                "dia": "2024-09-02",
                "titulo": "A - Reunião",
                "horario": "09h00",
                "local": "Palácio do Planalto",
            },
            {
                "dia": "2024-09-08",
                "titulo": "B - ESTE EVENTO",
                "horario": "02h30",
                "local": "Palácio do Planalto",
            },
            {
                "dia": "2024-09-08",
                "titulo": "C - EVENTO 2 APARECER",
                "horario": "05h30",
                "local": "Palácio do Planalto",
            },
            {
                "dia": "2024-09-02",
                "titulo": "D - Ministra do Meio Ambiente e Mudança do Clima, Marina Silva",
                "horario": "11h00",
                "local": "Palácio do Planalto",
            },
        ]

        self.assertEqual(menu.events_alphabetically_title(), expected_result)

    def test_events_alphabetically_location(self):
        with open("agenda_teste.json", "r", encoding="utf-8") as arquivo:
            events = json.load(arquivo)

        menu = Menu(events)

        expected_result = [
            {
                "dia": "2024-09-02",
                "titulo": "A - Reunião",
                "horario": "09h00",
                "local": "Palácio do Planalto",
            },
            {
                "dia": "2024-09-02",
                "titulo": "D - Ministra do Meio Ambiente e Mudança do Clima, Marina Silva",
                "horario": "11h00",
                "local": "Palácio do Planalto",
            },
            {
                "dia": "2024-09-08",
                "titulo": "B - ESTE EVENTO",
                "horario": "02h30",
                "local": "Palácio do Planalto",
            },
            {
                "dia": "2024-09-08",
                "titulo": "C - EVENTO 2 APARECER",
                "horario": "05h30",
                "local": "Palácio do Planalto",
            },
        ]

        self.assertEqual(menu.events_alphabetically_location(), expected_result)

    def test_events_ordered_date(self):
        with open("agenda_teste.json", "r", encoding="utf-8") as arquivo:
            events = json.load(arquivo)

        menu = Menu(events)

        expected_result = [
            {
                "dia": "2024-09-02",
                "titulo": "A - Reunião",
                "horario": "09h00",
                "local": "Palácio do Planalto",
            },
            {
                "dia": "2024-09-02",
                "titulo": "D - Ministra do Meio Ambiente e Mudança do Clima, Marina Silva",
                "horario": "11h00",
                "local": "Palácio do Planalto",
            },
            {
                "dia": "2024-09-08",
                "titulo": "B - ESTE EVENTO",
                "horario": "02h30",
                "local": "Palácio do Planalto",
            },
            {
                "dia": "2024-09-08",
                "titulo": "C - EVENTO 2 APARECER",
                "horario": "05h30",
                "local": "Palácio do Planalto",
            },
        ]

        self.assertEqual(menu.events_ordered_date(), expected_result)

    def test_events_ordered_hours(self):
        with open("agenda_teste.json", "r", encoding="utf-8") as arquivo:
            events = json.load(arquivo)

        menu = Menu(events)

        expected_result = [
            {
                "dia": "2024-09-08",
                "titulo": "B - ESTE EVENTO",
                "horario": "02h30",
                "local": "Palácio do Planalto",
            },
            {
                "dia": "2024-09-08",
                "titulo": "C - EVENTO 2 APARECER",
                "horario": "05h30",
                "local": "Palácio do Planalto",
            },
            {
                "dia": "2024-09-02",
                "titulo": "A - Reunião",
                "horario": "09h00",
                "local": "Palácio do Planalto",
            },
            {
                "dia": "2024-09-02",
                "titulo": "D - Ministra do Meio Ambiente e Mudança do Clima, Marina Silva",
                "horario": "11h00",
                "local": "Palácio do Planalto",
            },
        ]

        self.assertEqual(menu.events_ordered_hours(), expected_result)


if __name__ == "__main__":
    unittest.main()
