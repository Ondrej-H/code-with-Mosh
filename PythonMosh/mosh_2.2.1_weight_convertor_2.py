 
# Moshova varianta
weight = float(input("Weight: "))
unit = input("In (L)bs or (K)g: ")

if unit.upper() == "L":
    converted = weight * 0.45359237
    print(f"Your weight is {converted} kilos.")
elif unit.upper() == "K":
    converted = weight / 0.45
    print(f"Your weight is {converted} pounds.")
else:
    print("Invalid unit")


# Moje varianta
weight = float(input("Weight: "))

vstupni_jednotky = input("In (L)bs or (K)g: ")
vysledek = 0

if vstupni_jednotky == "L" or vstupni_jednotky == "l":
    vysledek = weight * 0.45359237
    nove_jednotky = "Kg"
elif vstupni_jednotky == "K" or vstupni_jednotky == "k":
    vysledek = weight * 2.20462262
    nove_jednotky = "Lbs"

print(f"Your weight in {nove_jednotky} is {vysledek}.")

# Alt 113 = q