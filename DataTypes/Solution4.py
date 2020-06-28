first_str= input('Enter the first sample string: ')
second_str= input('Enter the second sample string: ')

two_chars_first = first_str[:2]    # first two characters from first string
two_chars_second = second_str[:2]  # first two characters from second string

final_str = first_str.replace(two_chars_first, two_chars_second, 1) + " " + second_str.replace(two_chars_second, two_chars_first, 1)

print(f'Sample Strings: {first_str}, {second_str}')
print(f'Final Result after swap of first letters: {final_str}')

