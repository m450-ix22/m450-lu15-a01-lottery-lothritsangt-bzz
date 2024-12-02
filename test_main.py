"""
Module for testing main functionalities.
"""

import pytest

import main


@pytest.fixture
def mock_functions(monkeypatch):
    """Monkeypatch to replace the functions 'login', 'transfer_money', 'select_menu' and 'create_ticket' in main"""

    def dummy_login():
        """Dummy function to replace the function 'login' in main"""
        pass

    def dummy_transfer(person):
        """Dummy function to replace the function 'transfer_money' in main"""
        pass

    def dummy_select_menu():
        """Dummy function to replace the function 'select_menu' in main"""
        print('Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden')
        return input('')

    def dummy_ticket(person):
        """Dummy function to replace the function 'create_ticket' in main"""
        pass

    monkeypatch.setattr(main, 'login', dummy_login)
    monkeypatch.setattr(main, 'transfer_money', dummy_transfer)
    monkeypatch.setattr(main, 'select_menu', dummy_select_menu)
    monkeypatch.setattr(main, 'create_ticket', dummy_ticket)


def test_main_exit(capsys, monkeypatch, mock_functions):
    """Test the main function with the exit option"""
    inputs = iter(['Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    main.main()
    output = capsys.readouterr().out
    assert output == 'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden\n'


def test_main_money(capsys, monkeypatch, mock_functions):
    """Test the main function with the money transaction option"""
    inputs = iter(['A', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main()
    output = capsys.readouterr().out
    assert output == 'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden\n' \
                     'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden\n'


def test_main_ticket(capsys, monkeypatch, mock_functions):
    """Test the main function with the ticket creation option"""
    inputs = iter(['B', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main.main()
    output = capsys.readouterr().out
    assert output == 'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden\n' \
                     'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden\n'
