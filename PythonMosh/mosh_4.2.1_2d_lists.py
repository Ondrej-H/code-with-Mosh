
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matrix)
print("----------------------------------------------------------------")

# vypíše item s indexem 0, což je v tomto případě list [1, 2, 3]
print(matrix[0])
print("----------------------------------------------------------------")
# vypíše z itemu (= z listu) s indexem 0 item s indexem 1, což je 2
print(matrix[0][1])
print("----------------------------------------------------------------")

# nahradí z proměnné matrix z prvního itemu item s indexem 1 (což je 2) za 20
matrix[0][1] = 20
print(matrix[0][1])
print("----------------------------------------------------------------")

for row in matrix:
    for item in row:
        print(item)
