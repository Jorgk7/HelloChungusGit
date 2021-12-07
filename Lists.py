names = ['Jorge', 'Luciano', 'Sebastian', 'Matias', 'Emilio', 'Jose Joaquin', 'Rofoldo']
names[0] = 'Orito'
print(names[2:])
print(names)

# 2d Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)

# List Methods
numbers1 = [5, 2, 1, 7, 4]
# numbers1.append(20) - adds and puts item at the end of the list
# numbers1.insert(0, 10) - inserts item where you select of the list
# numbers1.remove(5) - removes item from the list
# numbers1.clear() - removes every item from the list
# numbers1.pop() - removes the last item from the list
# print(numbers1.index(5)) - checks the existence of an item in the list (use print(50 in numbers1) its better)
# print(numbers1.count(5)) - counts how many times the item is repeated
# numbers1.sort() - sorts the list in a ascending order
# numbers1.reverse() - sorts the list in a descending order
# numbers2 = numbers1.copy() - copies the list, whatever method you use on the first list wont affect this copy
numbers2 = numbers1.copy()
numbers1.append(20)
print(numbers1)
print(numbers2)
