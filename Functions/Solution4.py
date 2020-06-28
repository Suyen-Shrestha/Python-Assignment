sample_string = input('Enter a sample string to be reverse: ')


def reverse_str(input_str):
    reversed_str = ''
    for ch in input_str:
        reversed_str = ch + reversed_str
    return reversed_str

print(f'The original string: {sample_string}')
final_str = reverse_str(sample_string)
print(f'The reverse of the string: {final_str}')

