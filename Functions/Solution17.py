

# def starts_with(input_str,char):
#     return input_str.startswith(start_char)

starts_with = lambda st,ch: True if st.startswith(ch) else False

input_str = input('Enter a string: ')
input_char = input('Enter a character to check if the string starts with that character: ')

if starts_with(input_str,input_char):
    print(f'The string "{input_str}" contains "{input_char}"')
else:
    print(f'The string "{input_str}" doesnot contain "{input_char}"')
