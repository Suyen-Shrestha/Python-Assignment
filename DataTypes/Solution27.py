list1 = [1, 3, 5, 7, 9, 10]
list2 = [2, 4, 6, 8]

print(f'Sample lists before replacing last element on first list: {list1}, {list2}')

list1[-1:] = list2

print(f'Sample list after replacing last element on first list with second list: {list1}')

