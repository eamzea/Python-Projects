# -> Map creates a new list [3,6,9]
print(list(map(lambda item: item*3, [1, 2, 3])))


my_list = [5, 4, 3]

print(list(map(lambda item: item**2, my_list)))

a_list = [(0, 2), (4, 3), (9, 9), (10, -1)]

a_list.sort(key=lambda item: item[1])
