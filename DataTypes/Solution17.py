items_li = input('Enter the list of numbers separated by comma: ').split(',')
nums_li = [int(x.strip()) for x in items_li]
mul=1

for item in nums_li:
    mul *= item

print(f'The items in the list: {nums_li}')    
print(f'Multiple of items in list: {mul}')    