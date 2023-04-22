from datetime import datetime
import random


def time_decorator(func):
    def wrapper_func(*args):
        time = datetime.now()
        func(*args)
        print(f"{func}\t\t{datetime.now() - time}")
    return wrapper_func

@time_decorator
def check_string_dima(n):
    flag = True
    counts_of_dot = 0
    counts_of_minuses = 0
    for i in n:
        if i not in "1234567890.-":
            flag = False
        elif i in "-" and i != n[0]:
            flag = False
        elif i in "-":
            counts_of_minuses += 1
        elif i in ".":
            counts_of_dot += 1
    if counts_of_dot > 1 or counts_of_minuses > 1:
        flag = False
    if flag == False:
        return " Вы ввели не коректное число: " + n
    else:
        if n.isdigit():
            return "Вы ввели положительное целое число: " + n
        else:
            if float(n) % 1 != 0:
                if float(n) < 0:
                    return "Вы ввели отрицательное дробное число: " + n
                else:
                    return "Вы ввели положительное дробное число: " + n

@time_decorator
def check_string_lesha(string):
    if string.isdigit():
        return f"Вы ввели положительное целое число: {string}"
    for i in string:
        if "-0.123456789".find(i) == -1:
            return f"Вы ввели некорректное число: {string}"
    if string.count("-") > 1 or string.count(".") > 1 or string.find("-") > 0:
        return f"Вы ввели некорректное число: {string}"
    if string.find(".") != -1:
        if string.find("-") != -1:
            return f"Вы ввели отрицательное дробное число: {string}"
        else:
            return f"Вы ввели положительное дробное число: {string}"
    else:
        return f"Вы ввели отрицательное целое число: {string}"

def _already_has_dot(ch, is_float):
    return ch == '.' and is_float

@time_decorator
def check_string_petya(data):
    numbers_list = '0123456789.'
    is_negative, is_float = '-' == data[0], False

    for ch in data[1:] if is_negative else data:
        if _already_has_dot(ch, is_float) or ch not in numbers_list:
            return 'This is wrong number'

        is_float = ch == '.' or is_float

    return f'This is {"negative" if is_negative else "positive"} {"fractional number" if is_float else "integer"}'

@time_decorator
def check_string_max(str):
    minus_count = 0
    dot_count = 0
    if str.isdigit():
        return f"Вы ввели целое положительное число: {str}"
    for c in str:
        if c not in "-0.123456789":
            return f"Вы ввели некорректное число: {str}"
        if c in "-":
            minus_count += 1
            if minus_count > 1 or c != str[0]:
                return f"Вы ввели некорректное число: {str}"
        if c in ".":
            dot_count += 1
            if dot_count > 1:
                return f"Вы ввели некорректное число: {str}"
    if dot_count:
        if minus_count:
            return f"Вы ввели дробное отрицательное число: {str}"
        else:
            return f"Вы ввели дробное положительное число: {str}"
    return f"Вы ввели целое отрицательное число: {str}"


count = 1000000
sequence = [str(random.randint(0, 9)) for i in range(count)]
tests = []

test1 = sequence.copy()
tests.append("".join(test1))

test2 = sequence.copy()
test2[0] = "-"
tests.append("".join(test2))

test3 = sequence.copy()
test3[-2] = "."
tests.append("".join(test3))

test4 = sequence.copy()
test4[0] = "-"
test4[-2] = "."
tests.append("".join(test4))

test5 = sequence.copy()
test5[count // 2] = "A"
tests.append("".join(test5))

test6 = sequence.copy()
test6[0] = "-"
test6[count // 2] = "A"
tests.append("".join(test6))

test7 = sequence.copy()
test7[count // 2] = "A"
test7[-2] = "."
tests.append("".join(test7))

test8 = sequence.copy()
test8[0] = "-"
test8[count // 2] = "A"
test8[-2] = "."
tests.append("".join(test8))


for test in tests:
    print(f"{test[0:2]}{test[count // 2]}{test[-2:]}")
    check_string_dima(test)
    check_string_lesha(test)
    check_string_petya(test)
    check_string_max(test)
    print()