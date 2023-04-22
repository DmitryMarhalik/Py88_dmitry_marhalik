import json

data_base = {}


def get_name():
    return input("Enter name: ")


def check_name(name):
    if len(name) < 2:
        print("Error.The name is too short."
              "The name must contain more than 1 character")
    elif len(name) > 10:
        print("Error.The name is too long."
              "The name must contain less than 11 character")
    else:
        return name


def get_password():
    return input("Enter password: ")


def check_password(password):
    if nm not in data_base:
        print("Authentification Error. Check name")
    elif password == data_base[nm]:
        print(f"Hey,{nm}!")
        return True
    else:
        print("Authentification Error. Check password")


def registration():
    registr_name = input("Enter name to register: ")
    registr_password = input("Enter registration password: ")
    if registr_name in data_base:
        print("Your name has already been registered")
    else:
        data_base.update({registr_name: registr_password})
        with open("data_base_authentication.json", "w") as json_file:
            json.dump(data_base, json_file, indent=8)

    return data_base


while True:
    choice = input("For 'authentication' enter 'a' and press 'Enter',\n"
                   "For 'registration' enter 'r' and press 'Enter: \n")
    if choice == "a":
        nm = check_name(get_name())
        if nm:
            ps = check_password(get_password())
            if ps:
                break
    elif choice == "r":
        registration()
    else:
        print("Please, select 'a' or 'r'")
