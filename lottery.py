from numeric_input import read_int
from ticket import Ticket


def create_ticket(person):
    """
    creates a new lottery ticket
    """
    if person.balance >= 2.00:
        person.balance -= 2
        ticket = Ticket(0, list())
        select_numbers(ticket)
        print_ticket(ticket)
        print(f'Dein neues Guthaben: {person.balance:.2f}')
    else:
        print('Zuwenig Guthaben')


def select_numbers(ticket):
    """
    lets the user input his lottery numbers and joker number
    :param ticket:
    :return:
    """
    count = 0
    while count < 6:
        number = read_int(f'{count + 1}. Zahl: Geben Sie eine Zahl von 1 bis 42 ein > ', 1, 42)
        if number not in ticket.numbers:
            ticket.numbers.append(number)
            count += 1
        else:
            print('Diese Zahl haben Sie schon gewählt')

    ticket.joker = read_int('Jokerzahl: Geben Sie eine Zahl von 1 bis 6 ein > ', 1, 6)


def print_ticket(ticket):
    """
    prints the lottery ticket
    @param ticket: the ticket object
    """
    for count in range(1, 42):
        if count in ticket.numbers:
            print(f'{"X":>4}', end='')
        else:
            print(f'{count:4d}', end='')
        if count % 6 == 0:
            print()  # creates a new line
    print(f'\n\nJokerzahl: {ticket.joker:2d}')


if __name__ == '__main__':
    pass
