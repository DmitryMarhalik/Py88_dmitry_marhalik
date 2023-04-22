def one_function():
    """
    return name "one function"
    """
    print("one function")


def two_function():
    """
    return name "two function"
    """
    print("two function")


def three_function():
    """
    return name "three function"
    """
    print("three function")


def high_function(func, n=10):
    for i in range(1, n + 1):
        print(i, end=" ")
        func()


high_function(one_function, 3)
high_function(two_function, 5)
high_function(three_function, 10)
high_function(three_function)
