
age = 16
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")
print("__________________________")
# ---->

if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"
print(message)
print("__________________________")
# ---->

message = "Eligible" if age >= 18 else "Not eligible"
print(message)
