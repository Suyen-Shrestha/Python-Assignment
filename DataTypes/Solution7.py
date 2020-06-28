sample_str_list = input('Enter the list of words separated by space to find the longest length: ')

str_list = sample_str_list.split()
longest_len = 0

for st in str_list:
    if len(st) > longest_len:
        longest_len = len(st)

print(f'The length of the longest string is: {longest_len}')        