some_names = ("Dima", "Tanya", "Yan", "Mat", "Yaroslav", "Nikolay", "Ed")
result = tuple(filter(lambda i: len(i) > 4, some_names))
result_2 = tuple(filter(lambda i: len(i) <= 3, some_names))

print(result)
print(result_2)

# -----------------------------------------------------------------------------------#

some_names = ("Dima", "Tanya", "Yan", "Mat", "Yaroslav", "Nikolay", "Ed")


def name_length(names):
    return len(names) > 4


print(tuple(filter(name_length, some_names)))


def name_length(names):
    return len(names) <= 3


print(tuple(filter(name_length, some_names)))
