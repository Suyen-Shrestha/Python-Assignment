sample_str = input('Enter a non-empty string: ')
rem_index = int(input('Enter the index number to remove the character: '))
final_str = ''

if sample_str:
    final_str = sample_str.replace(sample_str[rem_index], '')
else:
    print("Please make sure you've enter a non-empty string!!")

print(f'Initial String: {sample_str}')
print(f'Final String: {final_str}')