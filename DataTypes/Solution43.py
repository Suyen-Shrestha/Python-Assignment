#Since tuple are immutable, we cannot remove elements from tuple.
#Converting tuple into list to remove items.

sample_tuple = ('a','e','i','o','u')
tuple_to_list = list(sample_tuple)

print(f'The sample tuple is: {sample_tuple}')
rem_item = input('Enter the item you want to remove from sample tuple: ')

if rem_item in tuple_to_list:
    tuple_to_list.remove(rem_item)

print(f'The final tuple after item removal: {tuple(tuple_to_list)}')    # converting the list back to tuple after removal of item.