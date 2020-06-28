items = input('Enter the list of items separated by comma: ').split(',')
items_li = [x.strip() for x in items]
unique_li = []

for item in items_li:
    if item not in unique_li:
        unique_li.append(item)

print(f'The original sample list: {items_li}')
print(f'The list after removing duplicates: {unique_li}')