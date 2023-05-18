import json
import re


class User:
    """Введенные данные пользователем"""

    def __init__(self, input_login, input_password, input_age=None):
        self.login = input_login
        self.password = input_password
        self.age = input_age

    def update_login_age(self, new_login, new_age):
        self.login = new_login
        self.age = new_age


class DataStorage:
    PATH_TO_STORE = "/home/dm/PycharmProjects/pythonProject/dmhome/lesson_11/data_base_authentication.json"

    @staticmethod
    def open_data():
        try:
            with open(DataStorage.PATH_TO_STORE, "r") as my_json_file:
                data_base = json.load(my_json_file)
        except FileNotFoundError:
            print("data_base file not found, please start registration")
            data_base = []
            data_base.append({"login": "1@gmail.com", "password": "0", "age": "0"})
            with open(DataStorage.PATH_TO_STORE, "w") as json_file:
                json.dump(data_base, json_file, indent=4)
        return data_base


class StartProgramm:
    @staticmethod
    def get_login():
        return input("Enter login: ")

    @staticmethod
    def get_password():
        return input("Enter password: ")

    @staticmethod
    def get_age():
        return input("Enter age: ")

    @staticmethod
    def start():
        choosing_an_action = input("\nfor 'authentication' enter 'a' and press 'Enter'\n"
                                   "for 'registration' enter 'r' and press 'Enter': \n")
        if choosing_an_action == "a":
            login, password = StartProgramm.get_login(), StartProgramm.get_password()
            if AuthenticationSystem.check_emaillogin(login):
                if AuthenticationSystem.check_len_login(login):
                    AuthenticationSystem().check_login_password(login, password)
        elif choosing_an_action == "r":
            login, password, age = StartProgramm.get_login(), StartProgramm.get_password(), StartProgramm.get_age()
            if AuthenticationSystem.check_emaillogin(login):
                if AuthenticationSystem.check_len_login(login):
                    RegistrationSystem().registration_name_and_passwords(login, password, age)
        else:
            print("Please, select 'a' or 'r'")


class AuthenticationSystem:
    """Проверка введенных данных пользователя"""

    @staticmethod
    def check_emaillogin(login):
        if re.fullmatch(r"[-a-z0-9!#\s%&'*+/=?^_`{|}~]+"
                        "(\.[-a-z0-9!#\s%&'*+/=?^_`{|}~]+"
                        ")*@{1}([a-z0-9]([-a-z0-9]{0,62}[a-z0-9])?)*", login):
            return True
        else:
            print("Enter your username as an email")
            return False

    @staticmethod
    def check_login_in_data_base(login):
        for user in data_base:
            if user["login"] == login:
                return True

    @staticmethod
    def check_len_login(login):
        if len(login) < 2:
            print("Error.The name is too short."
                  "The login must contain more than 1 character")
        elif len(login) > 25:
            print("Error.The name is too long."
                  "The login must contain less than 25 character")
        else:
            return login

    def chek_password(self, login, password):
        for user in data_base:
            if user["login"] == login and user["password"] == password in user.values():
                # if ("login", login) in i.items() and ("password", password) in i.items(): second version
                return True

    def check_login_password(self, login, password):
        if not AuthenticationSystem.check_login_in_data_base(login):
            print("Authentication Error. Check login")
        elif AuthenticationSystem.chek_password(self, login, password):
            print(f"Hey,{login}!")
            return True
        else:
            print("Authentication Error. Check password")


class RegistrationSystem(AuthenticationSystem):
    """Регистрация пользователя. Довавление имени и пароля пользователя в базу данных"""

    def registration_name_and_passwords(self, login, password, age):
        if AuthenticationSystem.check_login_in_data_base(login):
            print("Your login has already been registered")
        else:
            client = User(login, password, age)
            data_base.append({
                "login": client.login,
                "password": client.password,
                "age": client.age
            })
            print("You have been successfully registered")
            with open("data_base_authentication.json", "w") as json_file:
                json.dump(data_base, json_file, indent=4)
        return data_base


data_base = DataStorage.open_data()
StartProgramm.start()
