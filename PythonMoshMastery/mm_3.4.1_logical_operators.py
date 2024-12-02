
high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    message = "Eligible"
else:
    message = "Not eligible"
print(message)
print("________________________")
# ---->

message = "Eligible" if high_income or good_credit and not student else "Not eligible"
print(message)

message = "Eligible" if (high_income or good_credit) and not student else "Not eligible"
print(message)
