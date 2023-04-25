import json

with open("data_base_authentication.json", "r") as my_json_file:
    data_base = json.load(my_json_file)


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

try:
    class VerifyNamePassword(User):

        def check_name(self):
            if len(us.name) < 2:
                print("Error.The name is too short."
                      "The name must contain more than 1 character")
            elif len(us.name) > 15:
                print("Error.The name is too long."
                      "The name must contain less than 15 character")
            else:
                return us.name

        def check_password(self):
            if us.name not in data_base:
                print("Authentication Error. Check name")
            elif us.password == data_base[us.name]:
                print(f"Hey,{us.name}!")
                return True
            else:
                print("Authentication Error. Check password")


    class Registration(User):

        def registration_name_and_passwords(self):
            if us.name in data_base:
                print("Your name has already been registered")
            else:
                data_base.update({us.name: us.password})
                print("You have been successfully registered")
                with open("data_base_authentication.json", "a") as my_json_file:
                    json.dump(data_base, my_json_file, indent=4)
            return data_base


    while True:
        choice = input("For 'authentication' enter 'a' and press 'Enter',\n"
                       "For 'registration' enter 'r' and press 'Enter: \n")
        if choice == "a":
            us = User(input("Enter name: "), input("Enter password: "))
            varify_name = VerifyNamePassword.check_name(us.name)
            if varify_name:
                varify_password = VerifyNamePassword.check_password(us.password)
                if varify_password:
                    break
        elif choice == "r":
            us = User(input("Enter name: "), input("Enter password: "))
            varify_name = VerifyNamePassword.check_name(us.name)
            if varify_name:
                Registration.registration_name_and_passwords(us.password)
        else:
            print("Please, select 'a' or 'r'")
except KeyboardInterrupt:
    print("\n""You have STOPPED the execution of the program")
