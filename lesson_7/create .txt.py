one = input()
two = input()

with open("task2.txt", "w") as file:
    file.write(f"{one}\n{two}\n")

three = input()
four = input()

with open("task2.txt", "a") as file:
    file.write(f"{three}\n{four}\n")
