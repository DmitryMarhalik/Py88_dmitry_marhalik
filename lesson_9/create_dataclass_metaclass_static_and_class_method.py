from dataclasses import dataclass


@dataclass
class Football:
    team = "Juventus"
    country = "Italy"

    @staticmethod
    def st_meth():
        print("Hello")

    @classmethod
    def info(cls):
        print(f"{Football.team} {Football.country}")


class_1 = type("Metaclass", (), {"res": 3, "a1": 11})
# Football.info()
a = class_1()
print(Football.team)
