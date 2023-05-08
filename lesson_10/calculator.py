from custom_exceptions import checkup, check_digit

x = input("Enter the first digit:\n")
y = input("Enter the second digit: \n")
operation = input("Enter the operation: \n")
check_digit(x, y)
checkup(operation)
if operation == "+":
    print(int(x) + int(y))
elif operation == "-":
    print(int(x) - int(y))
elif operation == "*":
    print(int(x) * int(y))
elif operation == "**" or operation == "^":
    print(int(x) ** int(y))
else:
    try:
        print(int(x) / int(y))
    except ZeroDivisionError:
        print("Error, cannot be divided by zero.")
