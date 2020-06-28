
def check_upper_lower(input_str):
    upper_count = 0
    lower_count = 0
    for ch in input_str.replace(' ',''):
        if ch.isupper():
            upper_count += 1
        else:
            lower_count += 1
    return upper_count, lower_count

sample_str = input('Enter a sample sentence to count the no. of upper & lower characters:')
up_count,lo_count = check_upper_lower(sample_str)    
print(f'The total upper case characters: {up_count}')
print(f'The total lower case characters: {lo_count}')
