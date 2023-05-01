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


try:
    class AuthenticationSystem(User):
        """Проверка введенных данных пользователя"""

        @staticmethod
        def check_login_in_data_base():
            for i in data_base:
                if i["login"] == user.login:
                    return True

        # варианты проверки присутсвия логина в data_base:
        # return list(filter(lambda i: i == True,
        # (map(lambda i: i["login"] == user.login, data_base)))) ----> True or false

        # return bool(list(filter(lambda i: i['login'] == d, data_base))) -----> True or False

        # return (bool(next((i for i in lstdict if i["login"] == user.login),False)))

        @staticmethod
        def check_len_login():
            if len(user.login) < 2:
                print("Error.The name is too short."
                      "The login must contain more than 1 character")
            elif len(user.login) > 15:
                print("Error.The name is too long."
                      "The login must contain less than 15 character")
            else:
                return user.login

        @staticmethod
        def chek_password():
            for i in data_base:
                if user.login and user.password in i.values():
                    return True

        @staticmethod
        def check_login_password():
            if not AuthenticationSystem.check_login_in_data_base():
                print("Authentication Error. Check login")
            elif AuthenticationSystem.chek_password():
                print(f"Hey,{user.login}!")
            else:
                print("Authentication Error. Check password")


    class RegistrationSystem(User):
        """Регистрация пользователя. Довавление имени и пароля пользователя в базу данных"""

        @staticmethod
        def registration_name_and_passwords():
            if AuthenticationSystem.check_login_in_data_base():
                print("Your login has already been registered")
            else:
                data_base.append({
                    "login": user.login,
                    "password": user.password,
                    "age": user.age
                })
                print("You have been successfully registered")
                with open("data_base_authentication.json", "w") as json_file:
                    json.dump(data_base, json_file, indent=4)
            return data_base


    while True:
        choice = input("For 'authentication' enter 'a' and press 'Enter',\n"
                       "For 'registration' enter 'r' and press 'Enter: \n")
        if choice == "a":
            user = User(input("Enter login: "), input("Enter password: "))
            if AuthenticationSystem.check_len_login() and \
                    AuthenticationSystem.check_login_password():
                break
        elif choice == "r":
            user = User(input("Enter login: "), input("Enter password: "), input("Enter age: "))
            if AuthenticationSystem.check_len_login():
                RegistrationSystem.registration_name_and_passwords()
        else:
            print("Please, select 'a' or 'r'")
except KeyboardInterrupt:
    print("\nYou have STOPPED the execution of the program")
