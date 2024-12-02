
# removes duplicates in a list
list = [5, 2, 5, 1, 4, 7, 4, 1, 2]
uniques = []

for item in list:
    if item not in uniques:
        uniques.append(item)

print(uniques)