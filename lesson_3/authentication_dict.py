baza = {"Dima": "amid",
        "Oleg": "gelo",
        "Tanya": "aynat",
        "Liubov": "1234",
        "Yaroslav": "!!!",
        "Garry": "arvadekatava",
        "Vinny": "mupmurup"}


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
    if nm not in baza:
        print("Authentification Error. Check name")
    elif password == baza[nm]:
        print(f"Hey,{nm}!")
        return True
    else:
        print("Authentification Error. Check password")


while True:
    nm = check_name(get_name())
    if nm:
        ps = check_password(get_password())
        if ps:
            break
