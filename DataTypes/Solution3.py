sample_str = input('Enter a sample string: ')
first_char = sample_str[0]
new_str = sample_str.replace(first_char, '', 1)

if first_char in new_str:
    edited_str = new_str.replace(first_char, '$') 

final_str = first_char + edited_str  
  
print(f'Sample String: {sample_str}')    
print(f'Final Result: {final_str}')    

     