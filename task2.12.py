class TFaction:

    def __init__(self, floatNumber):
        self.left = int(floatNumber // 1)
        self.right=floatNumber%1
    def add(self,floatNumber):
        self.left+=int(floatNumber//1)
        self.right+=floatNumber%1
    def toString(self):
        return str(self.left+self.right)
    def sub(self,floatNumber):
        self.left -= int(floatNumber // 1)
        self.right -= floatNumber % 1

floatNumber=float(input("Введіть дробове число:"))
a=TFaction(floatNumber)
a.add(2.004)
print(a.toString())

