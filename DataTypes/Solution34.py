dic1={'red':1, 'blue':2}
dic2={'green':3, 'yellow':4}


new_dict = {**dic1, **dic2}

print(f'The two sample dictionaries are: {dic1}, {dic2}')
print(f'The final concatenated dictionary: {new_dict}')    