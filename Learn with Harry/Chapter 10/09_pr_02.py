class Calculator:
    def __init__(self, number) :
        self.number = number

    def square(self):
        print(f"The value of {self.number} square is {self.number ** 2}")
    
    def squareRoot(self):
        print(f"The value of {self.number} square is {self.number ** .5}")
    
    def cube(self):
        print(f"The value of {self.number} square is {self.number ** 3}")



a = Calculator(9)
a.square()
a.cube()
a.squareRoot()
