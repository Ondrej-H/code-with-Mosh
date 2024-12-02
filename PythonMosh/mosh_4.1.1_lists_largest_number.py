
numbers = [-100, -7, -5, -6, -2, 4, -9, 7, -3, -4, -6, -25, -5, -2, -7, -8]
largest = numbers[0]
#if numbers[0] > numbers[1]:
#    largest = numbers[0]
#else:
#    largest = numbers[1]
for number in numbers:
    if number > largest:
        largest = number
print(largest)