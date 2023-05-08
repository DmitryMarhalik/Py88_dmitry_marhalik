def check_digit(x, y):
    if not x.isdigit() or not y.isdigit():
        print("Please, enter the digits.\n")
        exit()


def checkup(operation):
    if operation not in ["+", "-", "/", "*", "**", "^"]:
        print("Please, enter the right operation.")
        exit()
