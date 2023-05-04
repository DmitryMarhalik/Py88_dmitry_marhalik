import json

with open("data_base_authentication.json", "r") as my_json_file:
    data_base = json.load(my_json_file)


# """преобразование изначальной базы данных"""
# def modify_dict():
#     list_base = []
#     for k, v in data_base.items():
#         list_base.append({"login": k, "password": v})
#     return list_base
#
#
# modify_base = modify_dict()


class DataStorage:
    PATH_TO_STORE = "/home/dm/PycharmProjects/pythonProject/dmhome/lesson_9/data_base_authentication.json"


class User:
    """Введенные данные пользователя"""

    def __init__(self, input_login, input_password, input_age=None):
        self.login = input_login
        self.password = input_password
        self.age = input_age

    def update_login_age(self, new_login, new_age):
        self.login = new_login
        self.age = new_age


class AuthenticationSystem():
    """Проверка введенных данных пользователя"""

    def check_login_in_data_base(self):
        for i in data_base:
            if i["login"] == client.login:
                return True

    # варианты проверки присутсвия логина в data_base:
    # return list(filter(lambda i: i == True,
    # (map(lambda i: i["login"] == user.login, data_base)))) ----> True or false

    # return bool(list(filter(lambda i: i['login'] == d, data_base))) -----> True or False

    # return (bool(next((i for i in lstdict if i["login"] == user.login),False)))

    def check_len_login(self):
        if len(client.login) < 2:
            print("Error.The name is too short."
                  "The login must contain more than 1 character")
        elif len(client.login) > 15:
            print("Error.The name is too long."
                  "The login must contain less than 15 character")
        else:
            return client.login

    def chek_password(self):
        for i in data_base:
            if client.login and client.password in i.values():
                return True

    def check_login_password(self):
        if not AuthenticationSystem.check_login_in_data_base(client.login):
            print("Authentication Error. Check login")
        elif AuthenticationSystem.chek_password(client.password):
            print(f"Hey,{client.login}!")
            return True
        else:
            print("Authentication Error. Check password")


class RegistrationSystem(AuthenticationSystem):
    """Регистрация пользователя. Довавление имени и пароля пользователя в базу данных"""

    def registration_name_and_passwords(self):
        if AuthenticationSystem.check_login_in_data_base(client.login):
            print("Your login has already been registered")
        else:
            data_base.append({
                "login": client.login,
                "password": client.password,
                "age": client.age
            })
            print("You have been successfully registered")
            with open("data_base_authentication.json", "w") as json_file:
                json.dump(data_base, json_file, indent=4)
        return data_base


while True:
    choosing_an_action = input("\nfor 'authentication' enter 'a' and press 'Enter'\n"
                               "for 'registration' enter 'r' and press 'Enter': \n")
    if choosing_an_action == "a":
        client = User(input("Enter login: "), input("Enter password: "))
        if RegistrationSystem.check_len_login(client.login) and \
                RegistrationSystem.check_login_password(client.password):
            break
    elif choosing_an_action == "r":
        client = User(input("Enter login: "), input("Enter password: "), input("Enter age: "))
        if RegistrationSystem.check_len_login(client.login):
            RegistrationSystem.registration_name_and_passwords(client.password)
    else:
        print("Please, select 'a' or 'r'")
