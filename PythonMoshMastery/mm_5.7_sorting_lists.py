
def sort_item(item):
    return item[1]


items = [
    ("Product3", 10),
    ("Product2", 9),
    ("Product1", 12)
]

# zde seřadí dle prvního itemu v tuplu
items.sort()
print(items)

# zde seřadí s pomocí funkce sort_item() podle druhého itemu v tuplu
items.sort(key=sort_item)
print(items)
