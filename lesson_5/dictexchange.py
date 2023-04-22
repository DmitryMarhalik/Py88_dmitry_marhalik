dict = {
    1: "qeqr",
    2: "wfefwr",
    3: "42525",
    "rest": (1, 2, 3),
    (3, 4, 5): (1, 2, 3),
    frozenset[1, 2]: "qwe"
}


def func(x):
    return {key: values for values, key in dict.items()}


new_dict = func(dict)
print(new_dict)


# Second version:
def func(x):
    for key, values in dict.items():
        key, values = values, key
        new.update({key: values})
    return new


new_dict = func(dict)
print(new_dict)
