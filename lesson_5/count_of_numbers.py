s = [1, 2, 3, 4, 6, 7, 3, 4, 43, 2, 1, 4, 2, 4]
dict = {}


def func(x):
    for i in x:
        dict.update({i: s.count(i)})
    return dict


func(s)
print(dict)

some_list = [1, 2, 4, 4, 7, 6, 1, 4, 5, 34, 6, 7, 86]
count_of_numbers = {}
for i in some_list:
    count_of_numbers[i] = count_of_numbers.get(i, 0) + 1
print(count_of_numbers)
