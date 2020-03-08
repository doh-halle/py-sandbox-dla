command = ""
started = False
stopped = False

while command != "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print('The car is already started!')
        else:
            started = True
            print("The Car is started")
    elif command == "stop":
        if stopped:
            print("The car is already started!")
        else:
            stopped = True
            print("The car is stopped")
    elif command == "help":
        print("""
    Start - to start the car
    stop - to stop the car
    Quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry I don't understand that")
