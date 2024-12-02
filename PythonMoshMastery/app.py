letters = ["a", "b", "c"]


# add
letters.append("d")
print(letters)

letters.insert(0, "-")
print(letters)


# remove
letters.pop(0)
print(letters)

letters.remove("b")
print(letters)

del letters[1:3]
print(letters)

letters.clear()
print(letters)
