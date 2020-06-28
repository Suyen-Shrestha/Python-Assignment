items_li = input('Enter the list of numbers separated by comma: ').split(',')
nums_li = [int(x.strip()) for x in items_li]

smallest_num = nums_li[0]

for num in nums_li:
    if num < smallest_num:
        smallest_num = num

print(f'The smallest no. in the list is: {smallest_num}')