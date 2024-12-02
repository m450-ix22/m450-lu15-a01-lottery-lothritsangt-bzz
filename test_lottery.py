import pytest
from unittest.mock import patch, MagicMock
from lottery import create_ticket, select_numbers, print_ticket
from ticket import Ticket


class MockPerson:
    def __init__(self, balance):
        self.balance = balance


def test_create_ticket_with_sufficient_balance():
    person = MockPerson(balance=5.00)
    with patch('lottery.select_numbers') as mock_select, patch('lottery.print_ticket') as mock_print:
        create_ticket(person)

    assert person.balance == 3.00  # 2€ sollten abgezogen sein
    mock_select.assert_called_once()  # Zahlen auswählen wurde aufgerufen
    mock_print.assert_called_once()   # Ticket drucken wurde aufgerufen


def test_create_ticket_with_insufficient_balance(capfd):
    person = MockPerson(balance=1.00)
    create_ticket(person)

    assert person.balance == 1.00  # Guthaben bleibt unverändert
    captured = capfd.readouterr()  # Terminal-Ausgabe abfangen
    assert "Zuwenig Guthaben" in captured.out


@patch('lottery.read_int', side_effect=[5, 12, 23, 34, 41, 7, 3])  # Mock Eingaben
def test_select_numbers(mock_read_int):
    ticket = Ticket(0, [])
    select_numbers(ticket)

    assert ticket.numbers == [5, 12, 23, 34, 41, 7]  # Die eingegebenen Zahlen
    assert ticket.joker == 3  # Joker-Zahl
    assert mock_read_int.call_count == 7  # 6 Zahlen + 1 Joker


def test_print_ticket(capfd):
    ticket = Ticket(joker=3, numbers=[1, 7, 12, 18, 23, 30])
    print_ticket(ticket)

    captured = capfd.readouterr()  # Terminal-Ausgabe abfangen
    output = captured.out
    # Überprüfe, ob X und Zahlen an den richtigen Stellen erscheinen
    assert "   X" in output
    assert "   1" not in output  # Die gewählten Zahlen sollten nicht angezeigt werden
    assert "Jokerzahl:  3" in output


if __name__ == '__main__':
    pytest.main()
