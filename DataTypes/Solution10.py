sample_str = input('Enter a sample string: ')
final_str = ''

for indx in range(len(sample_str)):
    if indx % 2 == 0:
        final_str = final_str + sample_str[indx] #only appending even indexed character in the final string.

print(f'Initial Sample String: {sample_str}')        
print(f'Final Resulting String: {final_str}')        
                
