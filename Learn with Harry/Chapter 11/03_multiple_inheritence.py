class Employee:
    company = "Visa"
    eCode = 120

class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1

class Programer(Freelancer, Employee):
    name = "Rohit"

p = Programer()
p.upgradeLevel()
print(p.level)
print(p.company)