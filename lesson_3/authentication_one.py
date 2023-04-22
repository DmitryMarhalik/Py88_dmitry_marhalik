def get_name():
    return input()


def check_name(name):
    if len(name) < 2:
        print("Error.The name is too short."
              "The name must contain more than 1 character")
    elif len(name) > 10:
        print("Error.The name is too long."
              "The name must contain less than 11 character")
    else:
        return name


func = check_name(get_name())
if func != None:
    print(f"Hello,{func}")
