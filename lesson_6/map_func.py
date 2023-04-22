list_of_numbers = [6, 7, 3, 8, 3, 2, 0, 3, 8, 1, 2324, 757, 0, 3, 4]


def check_number(num):
    if num % 2 == 0:
        return "четное"
    return "нечетное"


list_of_even_numbers = list(map(check_number, list_of_numbers))
result_dict = dict(zip(list_of_numbers, list_of_even_numbers))

print(result_dict)

#------------------------------------------------------------------#
# second version of dictionary creation:
list_of_numbers = [6, 7, 3, 8, 3, 2, 0, 3, 8, 1, 2324, 757, 0, 3, 4]


def check_number(num):
    if num % 2 == 0:
        return "четное"
    return "нечетное"


list_of_even_numbers = list(map(check_number, list_of_numbers))
result_dict = {}
for i in range(len(list_of_numbers)):
    result_dict[list_of_numbers[i]] = list_of_even_numbers[i]
print(result_dict)
