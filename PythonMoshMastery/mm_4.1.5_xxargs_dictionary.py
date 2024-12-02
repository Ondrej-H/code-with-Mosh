
def save_user(**user):      # ** vytvoří slovník
    print(user)


save_user()                 # to je on - prázdný slovník
# přijímá keyword arguments
save_user(id=1, name="John", age=22)
print("-----------------------------------------------------")

def save_user_keyword(**user):
    print(user["name"])             # or we can access specific keyword

save_user_keyword(id=2, name="Paul", age=50)