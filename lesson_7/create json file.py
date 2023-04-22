import json

dict = {123453: ("Dima", 19),
        134673: ("Oleg", 33),
        323764: ("Tanya", 14),
        423764: ("Vasya", 45),
        723764: ("Olya", 15),
        987653: ("Nikolay", 46)
        }
with open("my_json.json", "w") as json_file:
    json.dump(dict, json_file, indent=2)
