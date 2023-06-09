import json


class DataStorage:
    PATH_TO_STORE = "/home/dm/PycharmProjects/pythonProject/dmhome/lesson_10/data_base_authentication.json"

    def open_data(self):
        try:
            with open(DataStorage.PATH_TO_STORE, "r") as my_json_file:
                data_base = json.load(my_json_file)
        except FileNotFoundError:
            print("data_base file not found, please complete the registration")
            data_base = []
            with open(DataStorage.PATH_TO_STORE, "w") as json_file:
                json.dump(data_base, json_file, indent=4)
        return data_base


data_base = DataStorage().open_data()


class AuthenticationSystem:
    """Проверка введенных данных пользователя"""

    @staticmethod
    def check_login_in_data_base(login):
        for user in data_base:
            if user["login"] == login:
                return True

    @staticmethod
    def check_len_login(login):
        if 2 > len(login) or len(login) > 25:
            return False
        else:
            return login

    @staticmethod
    def chek_password(login, password):
        for user in data_base:
            if user["login"] == login and user["password"] == password in user.values():
                return True

    @staticmethod
    def check_login_password(login, password):
        if not AuthenticationSystem.check_login_in_data_base(login):
            return False
        elif AuthenticationSystem.chek_password(login, password):
            print(f"Hey,{login}!")
            return True
        else:
            return "Authentication Error. Check password"
