import json
from datetime import datetime, timedelta


class DataStorage:
    PATH_TO_STORE_prod_base = "/home/dm/PycharmProjects/pythonProject/dmhome/lesson_14/products_base.json"
    PATH_TO_STORE_datatime_base = "/home/dm/PycharmProjects/pythonProject/dmhome/lesson_14/datatime_base.json"

    @classmethod
    def open_databases(cls):
        try:
            with open(cls.PATH_TO_STORE_prod_base, "r") as my_json_file:
                products_base = json.load(my_json_file)
        except FileNotFoundError:
            print("products_base file not found, please add first product in products_base")
            products_base = []
            with open("products_base.json", "w") as json_file:
                json.dump(products_base, json_file, indent=4)
        try:
            with open(cls.PATH_TO_STORE_datatime_base, "r") as my_json_file:
                datatime_base = json.load(my_json_file)
        except FileNotFoundError:
            datatime_base = []
            with open("datatime_base.json", "w") as json_file:
                json.dump(datatime_base, json_file, indent=4)
        return products_base, datatime_base


class StartProgram:
    action= input("Select an action and press 'Enter': \n   'a' - to add product in database, \n"
                     "   'e' - to fix the meal time,\n   'c' - to calculate the result -->:\n    ")
    @classmethod
    def start(cls):
        if cls.action == "a":
            prod = Products(input("enter product: "), input("enter id of product: "), input("enter proteins: "),
                            input("enter fats: "), input("enter carbohydrates: "), input("enter Kcal: "))
            prod.products_base_update()
        elif cls.action == "e":
            eating_mael_time = EatingMeal(input("enter the 'id' of the product you have consumed: "),
                                          input("the amount consumed in food in gramms: "))
            id_in_base = bool(next((i for i in products_base if i["id"] == eating_mael_time.id), False))
            if not id_in_base:
                print("There is no such 'product id' in the database")
            else:
                eating_mael_time.add_datetime()
        elif cls.action == "c":
            day_ago = input("How many days ago to display the result? Enter days: \n")
            RequestCalculation().calculation(day_ago)


class Products:
    def __init__(self, product, id, proteins, fats, carbohydrates, calories):
        self.product = product
        self.id = id
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates
        self.calories = calories

    def products_base_update(self):
        id_prod_in_base = bool(next((i for i in products_base if i["id"] == self.id
                                     or i["product"] == self.product), False))
        if not id_prod_in_base:
            products_base.append({
                "id": self.id,
                "product": self.product,
                "proteins": self.proteins,
                "fats": self.fats,
                "carbohydrates": self.carbohydrates,
                "Kcal": self.calories
            })
            with open("products_base.json", "w") as json_file:
                json.dump(products_base, json_file, indent=4)
            return products_base
        else:
            print("Such a product already exists in the database")


class EatingMeal:
    def __init__(self, food_id, amount_of_food):
        self.id = food_id
        self.amount = amount_of_food

    def add_datetime(self):
        datatime_base.append({
            "id product": self.id,
            "amount of food": self.amount,
            "time of use": str(datetime.now())
        })
        with open("datatime_base.json", "w") as json_file:
            json.dump(datatime_base, json_file, indent=4)
        return datatime_base


class RequestCalculation:
    def calculation(self, day):
        self.day = day
        id_and_amount, products, proteins, fats, carbohydrates, Kcal = [], [], [], [], [], []
        day_ago = datetime.now() - timedelta(days=int(day))
        for dt in datatime_base:
            ob_data = datetime.strptime(dt["time of use"], "%Y-%m-%d %H:%M:%S.%f")
            if day_ago <= ob_data:
                id_and_amount.append([dt["id product"], dt["amount of food"]])
                print(id_and_amount)
        for value in products_base:
            for rslt in id_and_amount:
                if value["id"] == rslt[0]:
                    products.append(value["product"])
                    proteins.append((float(value["proteins"]) * (float(rslt[1]) / 100)))
                    fats.append((float(value["fats"])) * (float(rslt[1]) / 100))
                    carbohydrates.append((float(value["carbohydrates"])) * (float(rslt[1]) / 100))
                    Kcal.append((float(value["Kcal"])) * (float(rslt[1]) / 100))
        products_view = ", ".join(products)
        print((f"Нou have eaten the following foods: {products_view}.\n"
               f"Total amount of protein: {sum(proteins)} gr; fats: {sum(fats)} gr; "
               f"carbohydrates: {sum(carbohydrates)} gr; Kcal: {sum(Kcal)}"))


products_base, datatime_base = DataStorage.open_databases()
StartProgram().start()
