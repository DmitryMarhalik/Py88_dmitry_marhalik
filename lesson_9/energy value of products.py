import datetime
import json

with open("products_base.json", "r") as my_json_file:
    products_base = json.load(my_json_file)

with open("datatime_base.json", "r") as json_file:
    datatime_base = json.load(json_file)


class Products:

    def __init__(self, product, index, proteins, fats, carbohydrates, calories):
        self.product = product
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates
        self.calories = calories
        self.index = index

    def product_base_update(self):
        index_in_base = bool(next((i for i in products_base if i["index"] == prod.index), False))
        if not index_in_base:
            products_base.append({
                "index": self.index,
                "product": self.product,
                "proteins": self.proteins,
                "fats": self.fats,
                "carbohydrates": self.carbohydrates,
                "calories": self.calories
            })
            with open("products_base.json", "w") as json_file:
                json.dump(products_base, json_file, indent=4)
            return products_base
        else:
             print("Such a product index already exists in the database")

class EatingMeal:
    def __init__(self, food_index, amount_of_food):
        self.food = food_index
        self.amount = amount_of_food

    def add_date(self):
        datatime_base.append({
            "index of product": self.food,
            "time of use": str(datetime.datetime.now())
        })

        with open("datatime_base.json", "w") as json_file:
            json.dump(datatime_base, json_file, indent=4)
        return datatime_base


prod = Products(input("enter product: "), input("enter index of product: "), input("enter proteins: "),
                input("enter fats: "), input("enter carbohydrates: "), input("enter calories: "))
prod.product_base_update()

eating_mael_time = EatingMeal(input("enter the 'index' of the product you have consumed: "),
                              input("the amount consumed in food in gramms: "))
eating_mael_time.add_date()


# Написать консольное приложение для отслеживания потребления БЖУ и энергетической ценности продуктов.
#
# Приложение должно иметь возможность пополнять базу продуктов.
# Приложение должно иметь возможность выдавать данные о потреблении пользователем БЖУ и энергетической ценности
# в виде ккал за:
# 1. последний день
# 2. последние 3 дня
# 3. последние 7 дней
# 4. последние 30 дней
#
# workflow:
# выбор между:
# 1. внесением нового продукта с БЖУ и калорийностью
# 2. внесением данных об употреблении пользователем в пищу какого либо имеющегося в базе продукта в граммах
# 3. выводом колличества употребленных БЖУ и ккал за срок в днях.
#
# >1 -> вводим название продукта, вводим колличество БЖУ продукта рассчитанного на 100гр,
# вводим колличество ккал на 100гр.
# -> присваеваем уникальный индекс (число) данному продукту -> сохраняем в JSON файл с продуктами.
# >2 -> вводим индекс продукта и колличество употребленное в пищу в граммах -> присваеваем дату
# и время приему пищи ->
# сохраняем данные в JSON файл с приемами пищи
# >3 -> вводим вариант за какое колличество дней нужны данные -> выводим в консоль сумму Белков,
# \Жиров, Углеводов и ККал употребленных за
# это колличество дней
