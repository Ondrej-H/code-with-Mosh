
print("-------- C A R   G A M E --------")
command = ""
car_state = ""
exclamation_count = 1
while True:                          #command != "quit":
    command = input("> ").lower()
    if command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
            """)
    elif command == "start":
        if car_state == "started":
            started_yell = (f"The car is already started{exclamation_count * "!"}")
            print(started_yell)
            exclamation_count += 1
        else:
#           #elif car_state == "" or car_state == "stopped":
            exclamation_count = 1
            print("Car started... Ready to go!")
        car_state = "started"
    elif command == "stop":
        if car_state == "stopped":
            print("The car is already stopped!!!")
        else:
            print("Car stopped.")
        car_state = "stopped"
    elif command == "quit" or command == "q":
        print("Exiting the Car Game...")
        break
    else:
        print("I don't understand that...")