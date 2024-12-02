
def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welmoce aboard.")


print("Start")
greet_user(last_name="Smith", first_name="John")      #"John" a "Smith" jsou keyword arguments - pokud jsou tyto typy argumentů nakombinovány, veškeré keywords arguments musí přijít až po positional arguments (u positional arguments záleží na pořadí - na pozici)
greet_user("Mary", "Buddleblast")           #"Mary" a "Buddleblast" jsou positional arguments - záleží na jejich pořadí
print("Finish")