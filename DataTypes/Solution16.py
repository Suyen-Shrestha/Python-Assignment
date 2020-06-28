items_li = input('Enter the list of numbers separated by comma: ').split(',')
nums_li = [int(x.strip()) for x in items_li]
sum=0

for item in nums_li:
    sum += item

print(f'The items in the list: {nums_li}')    
print(f'Sum of items in list: {sum}')    