sample_str_li = input('Enter a list of strings separated by comma: ').split(',')
str_li = [x.strip(' ') for x in sample_str_li]  #removing leading & trailing white space in list of strings.

print(f'Before sorting, list of sample words: {str_li}')

unique_sorted_li = sorted(set(str_li))

print(f'Before sorting alphanumerically, list of unique sample words: {unique_sorted_li}')
