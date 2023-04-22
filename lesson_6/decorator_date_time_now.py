from datetime import datetime


def decorator(func_to_decorate):
    def wrapper(*args):
        print("<--start decoration-->")
        begin = datetime.now()
        func_to_decorate(*args)
        end = datetime.now()
        print("Время выполнения функции: ", end - begin)
        print("<--end decoration-->")

    return wrapper


@decorator
def first():
    print("My first decorated function!")


@decorator
def second(a, b):
    print(f"{a} в степени {b} = {a ** b}, My second decorated function!")


first()
second(5, 8)
