import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
MIN_DEPOSIT = 3

ROWS = 3
COLS = 3

symbol_count = {
    "A": 4,
    "B": 5,
    "C": 6,
    "D": 6
}

symbol_value = {
    "A": 3,
    "B": 2,
    "C": 1,
    "D": 1
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []

    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(column) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])



def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount >= MIN_DEPOSIT:
                break
            else:
                print(f"Deposit must be greater than or equal to ${MIN_DEPOSIT}.")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1 - " + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Lines must be between 1 - " + str(MAX_LINES) + ".")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if(total_bet > balance):
            print(f"You do not have enough to bet that amount, your balance is: ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on line(s):", *winning_lines)

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        if balance < MIN_DEPOSIT:
            depositAgain = input("You do not have enough money left to play. The game will end unless you make another deposit. Press 'd' to make another deposit.").lower()
            if depositAgain == "d":
                balance += deposit()
            else:
                break

        answer = input("Press enter to play. (q tp quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}.")

main()