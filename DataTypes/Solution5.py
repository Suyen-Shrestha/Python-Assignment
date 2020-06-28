sample_str = input('Enter a sample string: ')

final_str = ''

if len(sample_str) >= 3:
    if sample_str[-3:] == 'ing':
        final_str = sample_str + 'ly'
    else:
        final_str = sample_str + 'ing'
else:
    final_str = sample_str

print(f'Sample String: {sample_str}')
print(f'Final Result: {final_str}')
