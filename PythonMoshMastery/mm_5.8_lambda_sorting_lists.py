
items = [
    ("Product3", 10),
    ("Product2", 9),
    ("Product1", 12)
]

# seřadí s pomocí lambda podle druhého itemu v tuplu; lambda je anonymní funkce 
# - nemá slovo def, nemá název, nepoužívá slovo return, vrací výraz za dvojtečkou
#       zápis: lambda parameters:expresion
items.sort(key=lambda item: item[1])
print(items)
