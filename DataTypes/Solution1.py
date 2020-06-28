sample_str = input("Enter a sample string: ")
unique_chars_list = list(set(sample_str)) #list of unique characters in the sample string.
result = {}

for chl in unique_chars_list:
    result[chl] = 0
    for i in range(len(sample_str)):
        if chl == sample_str[i]:
            result[chl] += 1    

print(f'Sample String: {sample_str}')            
print(f'Frequency of Characters in the String: {result}')

