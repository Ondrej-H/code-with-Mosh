
# Saves user's name as input
name = input("Napište uživatelské jméno: ")

# Decides wheater name has no less than 3 characters and no more than 50 chars
# and print if ok or not ok
if len(name) < 3:
    print("Name must be at least 3 characters long.")
elif len(name) >50:
    print("Name must be a maximum of 50 characters.")
else:
    print("Name looks good.")