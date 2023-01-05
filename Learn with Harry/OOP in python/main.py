class Employee1:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary


harry = Employee1("Harry", "Shaikh", 44000)
rohan = Employee1("Rohan", "Islam", 44000)


print(harry.fname, "\n", rohan.fname)