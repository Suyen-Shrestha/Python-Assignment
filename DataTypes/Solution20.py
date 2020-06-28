str_li = input('Enter the list of strings separated by comma: ').split(',')
sample_str_li = [x.strip() for x in str_li]

count = 0

for item in sample_str_li:
    if len(item) >=2 and item[0] == item[-1]:
        count += 1

print(f'The sample list of strings: {sample_str_li}')        
print(f'No. of strings with length >= 2 and having the same first and last character: {count}')        
