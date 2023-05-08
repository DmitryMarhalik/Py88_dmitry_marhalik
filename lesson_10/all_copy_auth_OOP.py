import json


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
    PATH_TO_STORE = "/home/dm/PycharmProjects/pythonProject/dmhome/lesson_10/data_base_authentication.json"

    def open_data(self):
        try:
            with open(DataStorage.PATH_TO_STORE, "r") as my_json_file:
                data_base = json.load(my_json_file)
        except FileNotFoundError:
            print("data_base file not found, please complete the registration")
            data_base = []
            data_base.append({"login": "aa", "password": "0", "age": "0"})
            with open(DataStorage.PATH_TO_STORE, "w") as json_file:
                json.dump(data_base, json_file, indent=4)

        with open("data_base_authentication.json", "r") as my_json_file:
            data_base = json.load(my_json_file)
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

    def start(self):
        choosing_an_action = input("\nfor 'authentication' enter 'a' and press 'Enter'\n"
                                   "for 'registration' enter 'r' and press 'Enter': \n")
        if choosing_an_action == "a":
            login, password = StartProgramm.get_login(), StartProgramm.get_password()
            if AuthenticationSystem.check_len_login(self, login):
                AuthenticationSystem.check_login_password(self, login, password)
        elif choosing_an_action == "r":
            login, password, age = StartProgramm.get_login(), StartProgramm.get_password(), StartProgramm.get_age()
            # client = User(login, password, age)
            if AuthenticationSystem.check_len_login(self, login):
                RegistrationSystem.registration_name_and_passwords(self, login, password, age)
        else:
            print("Please, select 'a' or 'r'")


class AuthenticationSystem:
    """Проверка введенных данных пользователя"""

    def check_login_in_data_base(self, login):
        for i in data_base:
            if i["login"] == login:
                return True

    def check_len_login(self, login):
        if len(login) < 2:
            print("Error.The name is too short."
                  "The login must contain more than 1 character")
        elif len(login) > 15:
            print("Error.The name is too long."
                  "The login must contain less than 15 character")
        else:
            return login

    def chek_password(self, login, password):
        for i in data_base:
            if login and password in i.values():
                return True

    def check_login_password(self, login, password):
        if not AuthenticationSystem.check_login_in_data_base(self, login):
            print("Authentication Error. Check login")
        elif AuthenticationSystem.chek_password(self, login, password):
            print(f"Hey,{login}!")
            return True
        else:
            print("Authentication Error. Check password")


class RegistrationSystem(AuthenticationSystem):
    """Регистрация пользователя. Довавление имени и пароля пользователя в базу данных"""

    def registration_name_and_passwords(self, login, password, age):
        if AuthenticationSystem.check_login_in_data_base(self, login):
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


data_base = DataStorage().open_data()
StartProgramm().start()
