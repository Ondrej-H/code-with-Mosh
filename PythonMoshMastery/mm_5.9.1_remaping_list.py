
#   product name, price
items = [
    ("Product3", 10),
    ("Product2", 9),
    ("Product1", 12)
]

# přetransformuje (== přemapuje) seznam items na seznam s pouze druhou hodnotou z tuplu (price)
prices = []
for item in items:
    prices.append(item[1])

print(prices)