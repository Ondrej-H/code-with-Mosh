
# numbers.append(20)        připojí 20 na konec seznamu
# numbers.insert(0, 10)     na pozici s indexem 0 volží 10
# numbers.remove(5)         odstraní ze seznamu 5
# numbers.pop()             odstraní poslední objekt ze seznamu
# numbers.index(7)          returns index of first occurance of 7
# print(50 in numbers)      returns boolean value - je v seznamu nebo není v seznamu (True or False) - zde False
# print(numbers.count(1))  # returns count of 1s, zde 2
# numbers.sort()               # seřadí
# numbers.reverse()           # otočí od konce k začátku
# numbers2 = numbers.copy()     # vytvoří kopii listu
# numbers.clear()           vymaže vše ze seznamu

oddelovac = ("________________________")

numbers = [5, 2, 1, 7, 4, 1]
print(numbers)
print(oddelovac)

numbers.append(20)          # připojí 20 na konec seznamu
print(f"append 20 {numbers}")
print(oddelovac)

numbers.insert(0, 10)       # na pozici s indexem 0 volží 10
print(f"insert 10 {numbers}")
print(oddelovac)

numbers.remove(5)           # odstraní ze seznamu 5
print(f"remove 5 {numbers}")
print(oddelovac)

numbers.pop()               # odstraní poslední item ze seznamu
print(f"pop last {numbers}")
print(oddelovac)

numbers.index(7)            # returns index of first occurance of 7
print(f"index {numbers.index(7)}")
print(oddelovac)

# returns boolean value - je v seznamu nebo není v seznamu (True or False) - zde False
print(50 in numbers)
print(oddelovac)

print(f"počet jedniček: "{numbers.count(1)})      # returns count of 1s, zde 2
print(oddelovac)

numbers.reverse()           # otočí od konce k začátku
print(numbers)
print(oddelovac)

numbers.sort()               # seřadí
print(numbers)
print(oddelovac)

# otočí od konce k začátku - po předchozím použití .sort() od největšího po nejmenší
numbers.reverse()
print(numbers)
print(oddelovac)

numbers2 = numbers.copy()     # vytvoří kopii listu
print(numbers2)
print(oddelovac)

numbers.clear()             # vymaže vše ze seznamu
print(numbers)
print(oddelovac)
