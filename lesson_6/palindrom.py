some_names = ("Dima", "ded", "Yan", "zakaz", "Yaroslav", "RadaR", "Ed")


def check_palindrom(word):
    reverse_word = []
    for i in word:
        reverse_word.insert(0, i)  # добавление букв, получение списка из "перевернутого" слова
        str_word = ""
        for j in reverse_word:
            str_word += j  # перевод списка в строку через цикл
            if str_word == word:
                return word


print(tuple(filter(check_palindrom, some_names)))

# ----------------------------------------------------------------------------------------#
some_names = ("Dima", "ded", "Yan", "zakaz", "Yaroslav", "RadaR", "Ed")


def check_palindrom(word):
    reverse_word = []
    for i in word:
        reverse_word.insert(0, i)
    reverse_word = "".join(reverse_word)  # перевод списка в строку через метод "".join()
    if reverse_word == word:
        return word


print(tuple(filter(check_palindrom, some_names)))

# ----------------------------------------------------------------------------------------#
some_names = ("Dima", "ded", "Yan", "zakaz", "Yaroslav", "RadaR", "Ed")


def check_palindrom(word):
    reverse_word = ''
    for i in range(len(word) - 1, -1, -1):  # переворачивание строки через диапазон с отрицательным шагом
        reverse_word += word[i]
    if reverse_word == word:
        return reverse_word


print(tuple(filter(check_palindrom, some_names)))

# ----------------------------------------------------------------------------------------#
some_names = ("Dima", "ded", "Yan", "zakaz", "Yaroslav", "RadaR", "Ed")


def check_palindrom(word):
    if word[::-1] == word:  # переворачивание строки через срез с отрицательным шагом
        return word


print(tuple(filter(check_palindrom, some_names)))
