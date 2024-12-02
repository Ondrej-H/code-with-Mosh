
#Moshova varianta s použitím break
secret_number = 9
guess_limit = 3
guess_count = 0

while guess_count != guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry, you failed!")




# moje varianta (upravená)
secret_number = 8
guess_limit = 3
guess_count = 0

while guess_count != guess_limit:
    guess = int(input("Guess: "))
    if guess == secret_number:
        print("You won!")
        guess_count = guess_limit
    else:
        guess_count += 1
        if guess_count == guess_limit:
            print("You have failed!")