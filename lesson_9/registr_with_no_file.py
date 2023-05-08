import json
import os

PATH_TO_STORE = "/lesson_9/data_base_authentication.json"


class DataStorage:
    @staticmethod
    def isfile():
        if not os.path.isfile(PATH_TO_STORE):
            data_base = {}
            data_base.update({(user.name, user.password), ("age", user.age)})
            with open(PATH_TO_STORE, "w") as json_file:
                json.dump(data_base, json_file, indent=4)
            print("You have been successfully registered")
            return False
        else:
            with open("data_base_authentication.json", "r") as my_json_file:
                data_base = json.load(my_json_file)
                return data_base


class User:
    """Введенные данные пользователем"""

    def __init__(self, input_name, input_password, input_age=None):
        self.name = input_name
        self.password = input_password
        self.age = input_age

    def update_name_age(self, new_name, new_age):
        self.name = new_name
        self.age = new_age


try:
    """Проверка введенных данных пользователя"""


    class AuthenticationSystem(User):

        @staticmethod
        def check_name():
            if len(user.name) < 2:
                print("Error.The name is too short."
                      "The name must contain more than 1 character")
            elif len(user.name) > 15:
                print("Error.The name is too long."
                      "The name must contain less than 15 character")
            else:
                return user.name

        @staticmethod
        def check_password():
            if user.name not in data_base:
                print("Authentication Error. Check name")
            elif user.password == data_base[user.name]:
                print(f"Hey,{user.name}!")
                return True
            else:
                print("Authentication Error. Check password")


    class RegistrationSystem(User):
        """Регистрация пользователя. Довавление имени и пароля пользователя в базу данных"""

        @staticmethod
        def registration_name_and_passwords():
            if user.name in data_base:
                print("Your name has already been registered")
            else:
                data_base.update({(user.name, user.password), ("age", user.age)})
                print("You have been successfully registered")
                with open("data_base_authentication.json", "w") as json_file:
                    json.dump(data_base, json_file, indent=4)
            return data_base


    while True:
        choice = input("For 'authentication' enter 'a' and press 'Enter',\n"
                       "For 'registration' enter 'r' and press 'Enter: \n")
        if choice == "a":
            user = User(input("Enter name: "), input("Enter password: "))
            data_base = DataStorage.isfile()
            if AuthenticationSystem.check_name() and AuthenticationSystem.check_password():
                break
        elif choice == "r":
            user = User(input("Enter name: "), input("Enter password: "), input("Enter age: "))
            data_base = DataStorage.isfile()
            if not data_base:
                continue
            # AuthenticationSystem.check_name()
            if AuthenticationSystem.check_name():
                RegistrationSystem.registration_name_and_passwords()
        else:
            print("Please, select 'a' or 'r'")
except KeyboardInterrupt:
    print("\nYou have STOPPED the execution of the program")
