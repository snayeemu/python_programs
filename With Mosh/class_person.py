class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"{self.name} is talking now")


if __name__ == '__main__':
    person1 = Person("Nayeem")
    print(person1.name)
    person1.talk()