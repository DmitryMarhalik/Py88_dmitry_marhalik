import time


class Auto:
    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.color = "Black"
        self.mark = mark
        self.weight = "1650 kg"

    def move(self):
        print("Move--->")

    def stop(self):
        print("---<Stop!")

    def birthday(self):
        self.age += 1


my_car = Auto("VW", 11, "Passat")


class Truck(Auto):
    def __init__(self, max_load, brand, age, mark, color="White"):
        super().__init__(brand, age, mark)
        self.max_load = max_load
        self.color = color

    def move(self):
        print("attention!")
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, max_speed, brand, age, mark):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")


truck_1 = Truck(12000, "IVECO", 8, "Trakker")
truck_1.move()
truck_1.load()
print(truck_1.brand)
truck_1.birthday()
print(truck_1.age, "years")
print(truck_1.brand, end=" ")
print(truck_1.mark)
print(truck_1.color)
print(truck_1.max_load, "kg")

truck_2 = Truck(12430, "MAN", 5, "F2000", "Red")
truck_2.move()
truck_2.load()
print(truck_2.brand)
truck_2.birthday()
print(truck_2.age, "years")
print(truck_2.brand, end=" ")
print(truck_2.mark)
print(truck_2.color)
print(truck_2.max_load, "kg")

car_1 = Car(356, "Ferrari", 1, "SF90 Spider")
car_1.move()
print(car_1.brand, end=" ")
print(car_1.mark)
car_1.birthday()
print(car_1.age, "years")

car_2 = Car(350, "lamborghini", 0, "Revuelto")
car_2.move()
print(car_2.brand, end=" ")
print(car_2.mark)
car_2.birthday()
print(car_2.age, "years")
