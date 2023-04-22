def check_digit_in_string(n):
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
        print("Вы ввели некорретное число: ", n)
    else:
        if n.isdigit():
            print("Вы ввели положительное целое число:", n)
        else:
            if float(n) % 1 != 0:
                if float(n) < 0:
                    print("Вы ввели отрицательное дробное число:", n)
                else:
                    print("Вы ввели положительное дробное число:", n)
            else:
                print("Вы ввели отрицательное целое число:", n)


check_digit_in_string(input())
