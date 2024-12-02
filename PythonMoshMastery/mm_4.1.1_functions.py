
# we have two types of functions:
# 1 - perform a task
# 2 - return a value

# 1. perform a task
def greet(name):
    print(f"Hi {name}")


greet("Mosh")           # performing a task
print("---------------------------")
print(greet("Mosh"))    # calls the function (perform a task) and then returns default value None (because we haven't used the return statement)
print("---------------------------")
print("---------------------------")


# 2. return a value
# (for example function round(1.9) returns value 2
print(round(1.9))

def get_greeting(name):
    return f"Hi {name}"

# we still can just print it but what's more -->
print(get_greeting("Mosh"))
# we can store the returned value of the function in a variable:
message = get_greeting("Mosh")          # now we can reuse the function for example when working with files
file = open("content.txt", "w")         # we will learn about this two lines later
file.write(message)                     # now these serves just as an example
# or we can simply print the variable message
print(message)