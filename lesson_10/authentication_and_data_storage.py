import json


class DataStorage:
    PATH_TO_STORE = "/home/dm/PycharmProjects/pythonProject/dmhome/lesson_10/data_base_authentication.json"

    @staticmethod
    def open_data():
        try:
            with open(DataStorage.PATH_TO_STORE, "r") as my_json_file:
                data_base = json.load(my_json_file)
        except FileNotFoundError:
            print("data_base file not found, please complete the registration")
            data_base = []
            data_base.append({"login": "aa", "password": "0", "age": "0"})
            with open(DataStorage.PATH_TO_STORE, "w") as json_file:
                json.dump(data_base, json_file, indent=4)
        return data_base


data_base = DataStorage.open_data()


class AuthenticationSystem:
    """Проверка введенных данных пользователя"""

    @staticmethod
    def check_login_in_data_base(login):
        for i in data_base:
            if i["login"] == login:
                return True

    @staticmethod
    def check_len_login(login):
        if 2 > len(login) or len(login) > 15:
            return False
        else:
            return login

    def chek_password(self, login, password):
        for user in data_base:
            if user["login"] == login and user["password"] == password in user.values():
                return True

    def check_login_password(self, login, password):
        if not AuthenticationSystem.check_login_in_data_base(login):
            return False
        elif AuthenticationSystem.chek_password(self, login, password):
            print(f"Hey,{login}!")
            return True
        else:
            return "Authentication Error. Check password"
