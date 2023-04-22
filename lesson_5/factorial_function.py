def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(int(input())))


# Second version:

def fact(x):
    while x != 1:
        return x * fact(x - 1)
    return x


print(fact(int(input())))
