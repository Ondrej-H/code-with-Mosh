count_of_evens = 0
print("")
first_line = True
for number in range(1, 10):
    if first_line:
        if number % 2 == 0:
            count_of_evens += 1
            print("in numbers", number, end=" ")
            first_line = False
    else:
        if number % 2 == 0:
            count_of_evens += 1
            print(number, end=" ")
print(f"We have {count_of_evens} even numbers")
