
# removes duplicates in a list
list = [5, 2, 5, 1, 4, 7, 4, 1, 2]
for item in list:
    if list.count(item) > 1:
        list.remove(item)

print(list)


