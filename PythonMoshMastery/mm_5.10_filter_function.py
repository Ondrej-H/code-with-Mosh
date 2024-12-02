
#   product name, price
items = [
    ("Product3", 10),
    ("Product2", 9),
    ("Product1", 12)
]
print(f"\nList: {items}")

print(f"\nitems[0]: {items[0]}")
print(f"items[1]: {items[1]}")
print(f"items[3]: {items[2]}\n")

order = 1
for item in items:
    print(f"{order}. item: {item}:")
    print(f"item of 0: {item[0]}")
    print(f"item of 1: {item[1]}\n")
    order += 1

filtered_list = list(filter(lambda item: item[1] >= 10, items))
print(f"Filtered list (price >= 10): {filtered_list}")
