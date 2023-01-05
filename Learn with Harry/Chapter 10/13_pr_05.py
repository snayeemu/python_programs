class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("*************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train is {self.seats}")
        print("***************")

    def fareInfo(self):
        print(f"The price of the ticket is Tk {self.fare}")

    def bookTicket(self):
        if self.seats > 0:
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats -= 1
        else:
            print("Sorry this train is full! Kindly try in tatkal")

    def cancelTicket(self):
        print("Your seat is cancelled")
        self.seats += 1


intercity = Train("Intercity Express: 14015", 90, 2)
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()