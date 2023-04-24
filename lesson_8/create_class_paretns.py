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
my_car.move()
print(my_car.brand, end=" ")
print(my_car.mark)
print(my_car.age, "years")
print(my_car.weight)
my_car.stop()
my_car.birthday()
print(my_car.age)
