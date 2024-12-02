phone_number = input("Phone number: ")

digits = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
output = ""
for item in phone_number:
    output += digits.get(item, "!") + " "
print(output)