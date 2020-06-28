sample_list = [1,2,3,4]

final_list = []

print(f'The initial sample list: {sample_list}')

sample_str = input('Enter a sample string to append on each item on list: ')

for item in sample_list:
    final_list.append(sample_str + str(item))

print(f'The final list after appending string: {final_list}')