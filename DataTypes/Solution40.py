# tuples are immutable, so we cannot add an item in a tuple.
# Converting tuple into list to make this possible.

sample_tuple = (5,6,7,8,9)
converted_li = list(sample_tuple)

print(f'The sample tuple is: {sample_tuple}')

add_item = input('Enter an item you want to add in sample tuple: ')
converted_li.append(add_item)

print(f'The tuple after adding of item: {tuple(converted_li)}') #converting the list back to tuple after addition of item.