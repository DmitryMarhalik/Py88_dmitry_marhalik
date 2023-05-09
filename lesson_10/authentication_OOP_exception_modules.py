import json

from authentication_and_data_storage import AuthenticationSystem, data_base
from user import User


class StartProgram:
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
        while True:
            choosing_an_action = input("\nfor 'authentication' enter 'a' and press 'Enter'\n"
                                       "for 'registration' enter 'r' and press 'Enter': \n")
            if choosing_an_action == "a":
                login, password = StartProgram.get_login(), StartProgram.get_password()
                if AuthenticationSystem.check_len_login(login) and \
                        AuthenticationSystem().check_login_password(login, password):
                    break
                elif not AuthenticationSystem.check_login_in_data_base(login) or \
                        not AuthenticationSystem.check_len_login(login):
                    raise NameError

            elif choosing_an_action == "r":
                login, password, age = StartProgram.get_login(), StartProgram.get_password(), StartProgram.get_age()
                if AuthenticationSystem.check_len_login(login):
                    RegistrationSystem().registration_name_and_passwords(login, password, age)
                else:
                    raise NameError
            else:
                print("Please, select 'a' or 'r'")


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


StartProgram.start()
