
#   product name, price
items = [
    ("Product3", 10),
    ("Product2", 9),
    ("Product1", 12)
]

print(f"\nList: {items}\n")

prices_map_function = list(map(lambda item: item[1], items))
print(f"Prices mapped by map() function:\nlist(map(lambda item: item[1], items))\n--> {prices_map_function}\n")

prices_list_comprehension = [item[1] for item in items]     # tento zápis udělá naprosto to samé jako řádek 9 (jako list(map(...)))
print(f"Prices mapped by list comprehension:\n[item[1] for item in items]\n--> {prices_list_comprehension}\n")

prices_filter_function = list(filter(lambda item: item[1] >= 10, items))
print(f"Prices filtered by filter() function:\nlist(filter(lambda item: item[1] >= 10, items))\n--> {prices_filter_function}\n")

prices_filtered_by_list_comprehensions = [item for item in items if item[1] >= 10]
print(f"Prices filtered by list comprehensions:\n[item for item in items if item[1] >= 10]\n-- >{prices_filtered_by_list_comprehensions}")