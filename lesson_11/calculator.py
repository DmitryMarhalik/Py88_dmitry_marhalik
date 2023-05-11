import re


def check_expression(inpt):
    return re.match(r"^(\d+(\.\d+)?)(\s([\/\*\^\**\+\-]\s(\d+(\.\d+)?)))$", inpt)


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
    elif oper == "**" or oper == "^":
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

    ###################################################################################################

# expression = input("Please,enter the first, second numbers and operation separated by a space: ")
#
#
# def check_expression(inpt):
#     output = re.match(r"^(\d+(\.\d+)?)(\s([\/\*\^\**\+\-]\s(\d+(\.\d+)?)))$", inpt)
#     return output
#
#
# st = re.split(" ", expression)
# digit1 = st[0]
# oper = st[1]
# digit2 = st[2]
#
#
# def check_float():
#     for _ in st:
#         if "." in digit1 or "." in digit2:
#             if oper == "-":
#                 res = float(digit1) - float(digit2)
#             elif oper == "+":
#                 res = float(digit1) + float(digit2)
#             elif oper == "*":
#                 res = float(digit1) * float(digit2)
#             elif oper == "/":
#                 try:
#                     res = float(digit1) / float(digit2)
#                 except ZeroDivisionError:
#                     print("Error, cannot be divided by zero.")
#                     exit()
#             elif oper == "**" or oper == "^":
#                 res = float(digit1) ** float(digit2)
#             else:
#                 return "something went wrong"
#             return float(res)
#         return False
#
#
# ch = check_expression(expression)
# fl = check_float()
#
# if ch:
#     if fl:
#         print(fl)
#     elif oper == "-":
#         print(int(digit1) - int(digit2))
#     elif oper == "+":
#         print(int(digit1) + int(digit2))
#     elif oper == "**" or oper == "^":
#         print(int(digit1) ** int(digit2))
#     elif oper == "/":
#         try:
#             print(int(digit1) / int(digit2))
#         except ZeroDivisionError:
#             print("Error, cannot be divided by zero.")
#     elif oper == "*":
#         print(int(digit1) * int(digit2))
#     else:
#         print("something went wrong")
