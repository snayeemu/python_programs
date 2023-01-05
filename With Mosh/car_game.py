command = input('''start --> to start the car.
stop --> to stop the car.
quit --> to exit the game.

>   ''')

while True:
    if command.lower() == "start":
        print("Car started...Ready to go!")
    elif command.lower() == "stop":
        print("Car stopped.")
    elif command.lower() == "quit":
        break
    else:
        print("I don't understand that...")
    command = input(">   ")
