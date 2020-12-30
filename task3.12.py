from math import sqrt


class Pr:
    __a = 0
    __b = 0

    def __init__(self, x1, x2, y1, y2, x3, y3, ):
        self.a = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        self.b = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)

    def __getitem__(self, key):  # --- Для зчитування значення за індексом
        if key == 1:
            return self.a
        elif key == 2:
            return self.b

        else:
            raise Exception("Wrong key")

    def __setitem__(self, key, value):  # --- Для встановлення значення за індексом
        if key == 1:
            self.a = value
        elif key == 2:
            self.b = value

        else:
            raise Exception("Wrong key")

    def __delitem__(self, key):  # --- Видалення елемента за індексом
        if key == 1:
            del self.a
        elif key == 2:
            del self.b
        else:
            raise Exception("Wrong key")

    def getItem(self, side):
        if side == "a":
            return self.a
        elif side == "b":
            return self.b
        else:
            raise Exception("No more side")

    def setItem(self, value, side):
        if value >= 0:
            if side == "a":
                self.a = value
            elif side == "b":
                self.b =value
            else:
                raise Exception("No more side")
        else:
            raise Exception("value<0")

    def p(self):
        return ((sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))+(sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)))*2
    def s(self):
        return  sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) * sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)


x1=int(input("Введіть x1"))
x2=int(input("Введіть x2"))
x3=int(input("Введіть x3"))
y1=int(input("Введіть y1"))
y2=int(input("Введіть y2"))
y3=int(input("Введіть y3"))


c=Pr(x1, x2, y1, y2, x3, y3,)
print(c.getItem("a"))
c.setItem(3,"a")
print(c.getItem("a"))
print("s=",c.s())
print("p=",c.p())