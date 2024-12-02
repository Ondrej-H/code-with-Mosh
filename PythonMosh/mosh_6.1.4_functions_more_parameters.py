
def greet_user(first_name, nickname, last_name):
    print(f"Hi {first_name} '{nickname}' {last_name}")
    print("Welmoce aboard.")


print("Start")
greet_user("John", last_name="Smith", nickname="Buffalo")       #"John" a "Smith" jsou keyword arguments - pokud jsou tyto typy argumentů nakombinovány, veškeré keywords arguments musí přijít až po positional arguments (u positional arguments záleží na pořadí - na pozici)
greet_user("Mary", "Drywet", "Buddleblast")
print("Finish")