sample_dict = {'name': 'Harishankar', 'age': 25, 'city': 'kathmandu'}
sample_key = input('Enter a key to check if it exists in the sample dictionary: ')

if sample_key in sample_dict.keys():
    print(f"The key '{sample_key}' exists in the provided dictionary.")
else:
    print(f"The key '{sample_key}' doesnot exist in the provided dictionary.")

print(f'Sample Dictionary is: {sample_dict}')        