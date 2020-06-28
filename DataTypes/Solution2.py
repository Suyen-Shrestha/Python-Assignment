sample_str = input('Enter a sample string: ')
print(f'Sample String: {sample_str}')

if len(sample_str) >= 2:
    result = sample_str[:2] + sample_str[-2:]
    print(f'Expected Result: {result}')
else:
    result = 'Empty String'
    print(f'Final Result: {result}')                