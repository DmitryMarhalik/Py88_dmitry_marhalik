import json
import csv

with open("my_json.json", "r") as my_json_file:
    data_json = json.load(my_json_file)

with open("my_csv.csv", "w") as my_csv:
    writer = csv.writer(my_csv, delimiter=",")
    headers = [" "] + [f"person{i}" for i in range(1, len(data_json) + 1)]
    writer.writerow(headers)
    _id = ["id"] + [f"{i}" for i in data_json]
    writer.writerow(_id)
    name = ["name"] + [f"{data_json[i][0]}" for i in data_json]
    writer.writerow(name)
    age = ["age"] + [f"{data_json[i][1]}" for i in data_json]
    writer.writerow(age)
    phones = ["phone"] + ["097-32-88"] + ["097-33-88"] + ["697-32-88"] + ["097-32-48"] + ["297-32-88"] + ["764-32-88"]
    writer.writerow(phones)

# Second version:
# ------------------------------------------------------------------------------------------------#

import json
import csv

with open("my_json.json", "r") as my_json_file:
    data_json = json.load(my_json_file)
with open("my_csv.csv", 'w') as my_csv:
    writer = csv.writer(my_csv, delimiter=",")
    headers = ['  '] + [f'person {i}' for i in range(1, len(data_json) + 1)]
    writer.writerow(headers)
    _id = ['id']
    name = ['name']
    age = ['age']
    phone = ["phone"] + ["097-32-88"] + ["097-33-88"] + ["697-32-88"] + ["097-32-48"] + ["297-32-88"] + ["764-32-88"]
    for i, (username, ages) in data_json.items():
        _id.append(i)
        name.append(username)
        age.append(ages)

    writer.writerow(_id)
    writer.writerow(name)
    writer.writerow(age)
    writer.writerow(phone)
