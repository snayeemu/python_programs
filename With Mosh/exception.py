try:
    age = int(input("Age: "))
    income = 20000
    rist = income / age
    print(age)
except ZeroDivisionError:
    print("Age cannot be 0, ask your dad your age and try again")
except ValueError:
    print("Invalid value, read a book and try again")
