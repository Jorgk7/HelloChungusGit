# # Python Interpreter executes the code line to line from the top
# Tuples
# Tuples are numbers you cannot change remove or add items, you can only information about a tuple.
numbers = (1, 2, 3)
# numbers[0] = 10 - This will cause an error, since you cannot change a item.
print(numbers[2])

# Unpacking
coordinates = (1, 2, 3)
# coordinates[0] * coordinates[1] * coordinates[2] - Longest Way
# x = coordinates[0] - Long way
# y = coordinates[1]
# z = coordinates[2]
# Short Way - Also works with lists
x, y, z = coordinates
print(x)
print(y)
print(z)