dima = "Dima"
psdima = "amid"
oleg = "Oleg"
psoleg = "gelo"
tanya = "Tanya"
pstanya = "aynat"
yaroslav = "Yaroslav"
psyaroslav = "valsoray"
liubov = "Liubov"
psliubov = "vobuil"
names = (dima, oleg, tanya, yaroslav, liubov)
passwords = (psdima, psoleg, pstanya, psyaroslav, psliubov)


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
    if password in passwords and nm in names:
        print(f"Hey,{nm}!")
        return True
    else:
        print("Authentification Error. Check name or password!")


while True:
    nm = check_name(get_name())
    if nm:
        ps = check_password(get_password())
        if ps:
            break
