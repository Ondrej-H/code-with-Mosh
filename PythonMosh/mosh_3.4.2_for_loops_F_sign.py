
list = [5, 2, 5, 2, 2]
output = ""

for number in list:
    for x_count in range(0, number):
        output += "X"
    print(output)
    output = ""
