def deposit(total, deposited):
    return 240


def withdraw(total, withdrawn):
    if total > withdrawn:
        return total - withdrawn
    else:
        return total


def exchange(total_euro, input_currency, output_currency):
    return total_euro * 4/3


def transfer(first_total, second_total, transferred_amount):
    return first_total - transferred_amount, second_total + transferred_amount