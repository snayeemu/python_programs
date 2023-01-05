import math
class Circle:
    def setRadius(self, radius):
        self.radius = radius

    def getArea(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    c = Circle()
    radius = float(input("Enter radius: "))
    c.setRadius(radius)
    area = c.getArea()
    print("Area of the circle is: %.2f" %(area))