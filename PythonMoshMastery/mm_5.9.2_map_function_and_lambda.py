
#   product name, price
items = [
    ("Product3", 10),
    ("Product2", 9),
    ("Product1", 12)
]

# přetransformuje (== přemapuje) seznam items na seznam s pouze druhou hodnotou z tuplu (price)
iterable = map(lambda item: item[1], items)         # funkce map() vrací iterable; jako první param bere funkci - tedy lambdu, jako druhý param bere iterable
for item in iterable:
    print(item)

prices = list(map(lambda item: item[1], items))     # dělá to samé jako soubor 5.9.1_remaping_list - tedy vrací nový seznam
print(prices)
