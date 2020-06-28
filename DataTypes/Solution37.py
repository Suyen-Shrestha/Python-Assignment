sample_dict = {'red': 10, 'blue': 20, 'green': 30, 'black': 40}

mul = 1
for key in sample_dict:
    mul *= sample_dict[key]

print(f'The sample dictionary: {sample_dict}')
print(f'Multiplication of all items in the dictionary: {mul}')    
