
# unpacking and packing (*) lists
numbers = [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 9]
first, second, third, *other = numbers      # vytvoří ze zbytku itemů v listu nový list 'other'

print (first, second, third, other)

def multiply(*nums):
    print(nums)


multiply(1,2,3,4,5)

first, *other, last = numbers
print(first, last)
print(other)