sample_str = input('Enter a sample string: ')
final_str = ''

if sample_str:
    final_str = sample_str[-1:] + sample_str[1:-1] + sample_str[:1]
    print(f'The initial sample string: {sample_str}')    
    print(f'The final resulting string: {final_str}')
else:
    print('Please enter a non-empty string!')        