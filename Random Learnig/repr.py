from unicodedata import name


myList = [1, 2, 3, 4]
print(myList)

myDict = {'a' : 1, 'b' : 2}
print(myDict)

print(repr(myList))

class Car:
    def __init__(self, name, mileage) -> None:
        self.name = name
        self.mileage = mileage

    def __repr__(self) -> str:
        return "name: {}, mileage: {}".format(self.name, self.mileage)


c = Car("tesla", 270)
print(c)