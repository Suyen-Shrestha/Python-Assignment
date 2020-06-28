
def insert_string_middle(word, mid_string):
    """
        function for appending string in middle of another string.
    """
    mid_index = int(len(word) / 2)
    return word[:mid_index] + mid_string + word[mid_index:]

sample_str = input('Enter a sample string:')   
middle_str = input('Enter a string which you want to enter in middle:')

final_result = insert_string_middle(sample_str, middle_str)

print(f'The provided sample string: {sample_str}')
print(f'The provided middle string: {middle_str}')
print(f'The resultant final string: {final_result}')