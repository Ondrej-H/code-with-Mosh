
print("-------- C A R   G A M E --------")
command = ""
started = False
exclamation_count = 1
while True:                            #command != "quit":
    command = input("> ").lower()
    if command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
            """)
    elif command == "start":
        if started:                                 # == "started":
            started_yell = (f"The car is already started{exclamation_count * "!"}")
            print(started_yell)
            exclamation_count += 1
        else:
#           #elif started == "" or started == "stopped":
            exclamation_count = 1
            print("Car started... Ready to go!")
        started = True                              # "started"
    elif command == "stop":
        if not started:                             # "stopped":
            print("The car is already stopped!!!")
        else:
            started = False                             #"stopped"
            print("Car stopped.")
    elif command == "quit" or command == "q":
        print("Exiting the Car Game...")
        break
    else:
        print("I don't understand that...")