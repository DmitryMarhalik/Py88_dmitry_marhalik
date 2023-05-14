import re


def check_expression(inpt):
    return re.match(r"(\d+(\.\d+)?)(\s([/*^+-]\s(\d+(\.\d+)?)))", inpt)


def operation():
    if oper == "-":
        return digit1 - digit2
    elif oper == "*":
        return digit1 * digit2
    elif oper == "+":
        return digit1 + digit2
    elif oper == "/":
        try:
            return digit1 / digit2
        except ZeroDivisionError:
            return "Error, cannot be divided by zero"
    elif oper == "^":
        return digit1 ** digit2
    else:
        return "something went wrong"


def wrong():
    return "Incorrect input"


while True:
    expression = input("Please,enter the first, second numbers and operation separated by a space: ")

    if check_expression(expression):
        st = re.split(" ", expression)
        digit1 = float(st[0]) if "." in st[0] else int(st[0])
        oper = st[1]
        digit2 = float(st[2]) if "." in st[2] else int(st[2])
        print(operation())
    else:
        print(wrong())

    # version with lambda ##################################################################################
import re

while True:
    expression = input("Please,enter the first, second numbers and operation separated by a space: ")
    if re.match(r"^(\d+(\.\d+)?)(\s([/*^+-]\s(\d+(\.\d+)?)))$", expression):
        st = re.split(" ", expression)
        digit1 = float(st[0]) if "." in st[0] else int(st[0])
        digit2 = float(st[2]) if "." in st[2] else int(st[2])
        if st[1] == "-":
            res = lambda digit1, digit2: digit1 - digit2
            print(res(digit1, digit2))
        elif st[1] == "+":
            res = lambda digit1, digit2: digit1 + digit2
            print(res(digit1, digit2))
        elif st[1] == "*":
            res = lambda digit1, digit2: digit1 * digit2
            print(res(digit1, digit2))
        elif st[1] == "^":
            res = lambda digit1, digit2: digit1 ** digit2
            print(res(digit1, digit2))
        elif st[1] == "/":
            try:
                res = lambda digit1, digit2: digit1 / digit2
                print(res(digit1, digit2))
            except ZeroDivisionError:
                print("Error, cannot be divided by zero")
        else:
            print("Something went wrong")
    else:
        print("Incorrect input")

# short version ##########################################################################################
import re

while True:
    expression = input("Please,enter the first, second numbers and operation separated by a space: ")
    if re.match(r"^(\d+(\.\d+)?)(\s([/*^+-]\s(\d+(\.\d+)?)))$", expression):
        st = re.split(" ", expression)
        digit1 = float(st[0]) if "." in st[0] else int(st[0])
        digit2 = float(st[2]) if "." in st[2] else int(st[2])
        if st[1] == "-":
            print(f"result = {digit1 - digit2}")
        elif st[1] == "+":
            print(f"result = {digit1 + digit2}")
        elif st[1] == "*":
            print(f"result = {digit1 * digit2}")
        elif st[1] == "^":
            print(f"result = {digit1 ** digit2}")
        elif st[1] == "/":
            try:
                print(f"result = {digit1 / digit2}")
            except ZeroDivisionError:
                print("Error, cannot be divided by zero")
        else:
            print("Something went wrong")
    else:
        print("Incorrect input")
