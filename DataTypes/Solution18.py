items_li = input('Enter the list of numbers separated by comma: ').split(',')
nums_li = [int(x.strip()) for x in items_li]

largest_num = nums_li[0]

for num in nums_li[1:]:
    if num > largest_num:
        largest_num = num

print(f'The largest no. in the list is: {largest_num}')