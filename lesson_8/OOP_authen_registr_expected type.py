import json

with open("data_base_authentication.json", "r") as my_json_file:
    data_base = json.load(my_json_file)


class User:
    """Введенные данные пользователя"""

    def __init__(self):
        self.name = input("Enter name: ")
        self.password = input("Enter password: ")


try:
    class VerifyNamePassword(User):
        """Проверка введенных данных пользователя"""

        def check_name(self):
            if len(user.name) < 2:
                print("Error.The name is too short."
                      "The name must contain more than 1 character")
            elif len(user.name) > 15:
                print("Error.The name is too long."
                      "The name must contain less than 15 character")
            else:
                return user.name

        def check_password(self):
            if user.name not in data_base:
                print("Authentication Error. Check name")
            elif user.password == data_base[user.name]:
                print(f"Hey,{user.name}!")
                return True
            else:
                print("Authentication Error. Check password")


    class Registration(User):
        """Регистрация пользователя. Довавление имени и пароля пользователя в базу данных"""

        def registration_name_and_passwords(self):
            if user.name in data_base:
                print("Your name has already been registered")
            else:
                data_base.update({user.name: user.password})
                print("You have been successfully registered")
                with open("data_base_authentication.json", "w") as json_file:
                    json.dump(data_base, json_file, indent=4)
            return data_base


    while True:
        choice = input("For 'authentication' enter 'a' and press 'Enter',\n"
                       "For 'registration' enter 'r' and press 'Enter: \n")
        if choice == "a":
            user = User()
            varify_name_password = VerifyNamePassword.check_name(user.name), \
                VerifyNamePassword.check_password(user.password)
            if varify_name_password:
                break
        elif choice == "r":
            user = User()
            varify_name = VerifyNamePassword.check_name(user.name)
            if varify_name:
                Registration.registration_name_and_passwords(user.password)
        else:
            print("Please, select 'a' or 'r'")
except KeyboardInterrupt:
    print("\n""You have STOPPED the execution of the program")
